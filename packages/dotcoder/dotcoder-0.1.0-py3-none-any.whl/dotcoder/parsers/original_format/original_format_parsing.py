# This file is mainly kept as legacy so that we don't have to rewrite this code

from __future__ import annotations

import asyncio
import json
import logging
from asyncio import Event
from enum import Enum
from json import JSONDecodeError
from pathlib import Path
from typing import Any, AsyncGenerator

import attr
from termcolor import cprint

from dotcoder.code_file_manager import CodeFileManager
from dotcoder.config_manager import ConfigManager
from dotcoder.errors import ModelError
from dotcoder.parsers.change_display_helper import (
    change_delimiter,
    get_file_name,
    get_later_lines,
    get_line_number_buffer,
    get_previous_lines,
    get_removed_lines,
)
from dotcoder.parsers.file_edit import FileEdit
from dotcoder.streaming_printer import StreamingPrinter

from .original_format_change import OriginalFormatChange, OriginalFormatChangeAction


class _BlockIndicator(Enum):
    Start = "@@start"
    Code = "@@code"
    End = "@@end"


@attr.define
class ParsingState:
    message: str = attr.field(default="")
    cur_line: str = attr.field(default="")
    cur_printed: bool = attr.field(default=False)
    time_elapsed: float = attr.field(default=0)
    in_special_lines: bool = attr.field(default=False)
    in_code_lines: bool = attr.field(default=False)
    explanation: str = attr.field(default="")
    explained_since_change: bool = attr.field(default=True)
    code_changes: list[OriginalFormatChange] = attr.field(factory=list)
    json_lines: list[str] = attr.field(factory=list)
    code_lines: list[str] = attr.field(factory=list)
    rename_map: dict[Path, Path] = attr.field(factory=dict)

    def parse_line_printing(self, content: str):
        to_print = ""
        if self.cur_printed:
            to_print = content
        elif not self.could_be_special():
            to_print = self.cur_line
            self.cur_printed = True

        if not self.in_special_lines:
            self.explanation += to_print
            if to_print:
                self.explained_since_change = True

        return to_print

    def could_be_special(self):
        return any(
            len(self.cur_line.rstrip("\n")) <= len(to_match.value)
            and to_match.value.startswith(self.cur_line.rstrip("\n"))
            for to_match in _BlockIndicator
        )

    def create_code_change(self, code_file_manager: CodeFileManager):
        try:
            json_data = json.loads("\n".join(self.json_lines))
        except JSONDecodeError:
            raise ModelError(
                "Model gave malformed JSON for change",
                already_added_to_changelist=False,
            )

        new_change = OriginalFormatChange(
            json_data, self.code_lines, code_file_manager, self.rename_map
        )
        self.code_changes.append(new_change)
        self.json_lines, self.code_lines = [], []
        if new_change.action == OriginalFormatChangeAction.RenameFile:
            # This rename_map is a bit hacky; it shouldn't be used outside of streaming/parsing
            self.rename_map[new_change.name] = new_change.file

    def new_line(self, code_file_manager: CodeFileManager):
        to_print = ""
        entered_code_lines = False
        exited_code_lines = False
        created_code_change = False
        match self.cur_line.rstrip("\n"):
            case _BlockIndicator.Start.value:
                if self.in_special_lines or self.in_code_lines:
                    raise ModelError(
                        "Model gave start indicator while making change",
                        already_added_to_changelist=True,
                    )
                self.in_special_lines = True
            case _BlockIndicator.Code.value:
                if not self.in_special_lines:
                    raise ModelError(
                        "Model gave code indicator while it was not making a change",
                        already_added_to_changelist=False,
                    )
                if self.in_code_lines:
                    raise ModelError(
                        "Model gave code indicator while in code block",
                        already_added_to_changelist=True,
                    )
                self.in_code_lines = True
                self.create_code_change(code_file_manager)
                if not self.code_changes[-1].has_additions():
                    raise ModelError(
                        "Model gave code indicator for action without code",
                        already_added_to_changelist=True,
                    )
                entered_code_lines = True
                created_code_change = True
            case _BlockIndicator.End.value:
                if not self.in_special_lines:
                    raise ModelError(
                        "Model gave end indicator while not creating change",
                        already_added_to_changelist=False,
                    )
                if not self.in_code_lines:
                    self.create_code_change(code_file_manager)
                    created_code_change = True
                else:
                    self.code_changes[-1].code_lines = self.code_lines
                    self.code_lines = []
                    exited_code_lines = True
                self.in_special_lines, self.in_code_lines = False, False
            case _:
                if self.in_code_lines:
                    self.code_lines.append(self.cur_line.rstrip("\n"))
                elif self.in_special_lines:
                    self.json_lines.append(self.cur_line)
                elif not self.cur_printed:
                    self.explanation += self.cur_line
                    if self.cur_line:
                        self.explained_since_change = True

                if not self.cur_printed and (
                    self.in_code_lines or not self.in_special_lines
                ):
                    # Lets us print lines that start with @@start
                    to_print = self.cur_line

        self.cur_line = ""
        self.cur_printed = False
        return to_print, entered_code_lines, exited_code_lines, created_code_change


async def stream_and_parse_llm_response(
    response: AsyncGenerator[Any, None],
    code_file_manager: CodeFileManager,
    config: ConfigManager,
    shutdown: Event,
) -> tuple[str, list[FileEdit]]:
    state = ParsingState()
    printer = StreamingPrinter()
    printer_task = asyncio.create_task(printer.print_lines())
    try:
        if await _process_response(
            state, response, printer, code_file_manager, shutdown
        ):
            printer.wrap_it_up()
            await printer_task
        else:
            printer_task.cancel()
    except ModelError as e:
        logging.info(f"Model created error {e}")
        printer.wrap_it_up()
        # make sure we finish printing everything model sent before we encountered the crash
        await printer_task
        cprint("\n\nFatal error while processing model response:", "red")
        cprint(str(e), color="red")
        cprint("Using response up to this point.")
        if e.already_added_to_changelist:
            state.code_changes = state.code_changes[:-1]
    finally:
        logging.debug(f"LLM response:\n{state.message}")

    code_changes = list(filter(lambda change: not change.error, state.code_changes))
    return (state.message, OriginalFormatChange.to_file_edits(code_changes, config))


async def _process_response(
    state: ParsingState,
    response: AsyncGenerator[Any, None],
    printer: StreamingPrinter,
    code_file_manager: CodeFileManager,
    shutdown: Event,
) -> bool:
    def chunk_to_lines(chunk: Any) -> list[str]:
        return chunk["choices"][0]["delta"].get("content", "").splitlines(keepends=True)

    async for chunk in response:
        for content_line in chunk_to_lines(chunk):
            if content_line:
                state.message += content_line
                _process_content_line(state, content_line, printer, code_file_manager)
        if shutdown.is_set():
            if state.in_code_lines:
                state.code_changes = state.code_changes[:-1]
            return False

    # This newline solves at least 5 edge cases singlehandedly
    _process_content_line(state, "\n", printer, code_file_manager)

    # If the model forgot an @@end at the very end of it's message, we might as well add the change
    if state.in_special_lines:
        logging.info("Model forgot an @@end!")
        _process_content_line(state, "@@end\n", printer, code_file_manager)
    return True


def _process_content_line(
    state: ParsingState,
    content: str,
    printer: StreamingPrinter,
    code_file_manager: CodeFileManager,
):
    beginning = state.cur_line == ""
    state.cur_line += content

    if (
        state.in_code_lines and not state.code_changes[-1].error
    ) or not state.in_special_lines:
        to_print = state.parse_line_printing(content)
        prefix = (
            "+" + " " * (get_line_number_buffer(state.code_changes[-1].file_lines) - 1)
            if state.in_code_lines and beginning
            else ""
        )
        color = "green" if state.in_code_lines else None
        if to_print:
            printer.add_string(prefix + to_print, end="", color=color)

    if "\n" in content:
        (
            to_print,
            entered_code_lines,  # pyright: ignore[reportUnusedVariable]
            exited_code_lines,
            created_code_change,
        ) = state.new_line(code_file_manager)

        if created_code_change:
            cur_change = state.code_changes[-1]
            if cur_change.error:
                logging.info(
                    f"Model error when creating code change: {cur_change.error}"
                )
                printer.add_string("\nNot showing skipped change due to error:")
                printer.add_string(cur_change.error, color="red")
                printer.add_string(
                    "Continuing model response...\n", color="light_green"
                )
            else:
                display_information = cur_change.get_change_display_information()
                if (
                    len(state.code_changes) < 2
                    or state.code_changes[-2].file != cur_change.file
                    or state.explained_since_change
                    or state.code_changes[-1].action
                    == OriginalFormatChangeAction.RenameFile
                ):
                    printer.add_string(get_file_name(display_information))
                    if cur_change.has_additions() or cur_change.has_removals():
                        printer.add_string(change_delimiter)
                state.explained_since_change = False
                printer.add_string(get_previous_lines(display_information))
                printer.add_string(get_removed_lines(display_information))
                if not cur_change.has_additions() and cur_change.has_removals():
                    printer.add_string(get_later_lines(display_information))
                    printer.add_string(change_delimiter)

        if to_print and not (state.in_code_lines and state.code_changes[-1].error):
            prefix = (
                "+"
                + " " * (get_line_number_buffer(state.code_changes[-1].file_lines) - 1)
                if state.in_code_lines and beginning
                else ""
            )
            color = "green" if state.in_code_lines else None
            printer.add_string(prefix + to_print, end="", color=color)
        if exited_code_lines and not state.code_changes[-1].error:
            printer.add_string(
                get_later_lines(state.code_changes[-1].get_change_display_information())
            )
            printer.add_string(change_delimiter)
