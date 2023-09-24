from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

from termcolor import colored, cprint

from .code_context import CodeContext
from .code_file import CodeFile
from .errors import DotcoderError
from .git_handler import commit


class Command(ABC):
    # Unfortunately, Command isn't defined here yet, so even with annotations we need quotation marks
    _registered_commands = dict[str, type["Command"]]()

    def __init_subclass__(cls, command_name: str | None) -> None:
        if command_name is not None:
            Command._registered_commands[command_name] = cls

    @classmethod
    def create_command(
        cls, command_name: str, code_context: Optional[CodeContext] = None
    ) -> Command:
        if command_name not in cls._registered_commands:
            return InvalidCommand(command_name)

        command_cls = cls._registered_commands[command_name]
        if command_cls in [AddCommand, RemoveCommand]:
            if code_context is None:
                raise DotcoderError(
                    f"Code context must be provided for {command_cls.__name__}"
                )
            return command_cls(code_context)
        else:
            return command_cls()

    @classmethod
    def get_command_completions(cls) -> List[str]:
        return list(map(lambda name: "/" + name, cls._registered_commands))

    @abstractmethod
    def apply(self, *args: str) -> None:
        pass

    # TODO: make more robust way to specify arguments for commands
    @classmethod
    @abstractmethod
    def argument_names(cls) -> list[str]:
        pass

    @classmethod
    @abstractmethod
    def help_message(cls) -> str:
        pass


class InvalidCommand(Command, command_name=None):
    def __init__(self, invalid_name: str):
        self.invalid_name = invalid_name

    def apply(self, *args: str) -> None:
        cprint(
            f"{self.invalid_name} is not a valid command. Use /help to see a list of"
            " all valid commands",
            color="light_yellow",
        )

    @classmethod
    def argument_names(cls) -> list[str]:
        raise DotcoderError("Argument names called on invalid command")

    @classmethod
    def help_message(cls) -> str:
        raise DotcoderError("Help message called on invalid command")


help_message_width = 60


class HelpCommand(Command, command_name="help"):
    def apply(self, *args: str) -> None:
        if not args:
            commands = Command._registered_commands.keys()
        else:
            commands = args
        for command_name in commands:
            if command_name not in Command._registered_commands:
                message = colored(
                    f"Error: Command {command_name} does not exist.", color="red"
                )
            else:
                command_class = Command._registered_commands[command_name]
                argument_names = command_class.argument_names()
                help_message = command_class.help_message()
                message = (
                    " ".join(
                        [f"/{command_name}"] + [f"<{arg}>" for arg in argument_names]
                    ).ljust(help_message_width)
                    + help_message
                )
            print(message)

    @classmethod
    def argument_names(cls) -> list[str]:
        return []

    @classmethod
    def help_message(cls) -> str:
        return "Displays this message"


class CommitCommand(Command, command_name="commit"):
    default_message = "Automatic commit"

    def apply(self, *args: str) -> None:
        if args:
            commit(args[0])
        else:
            commit(self.__class__.default_message)

    @classmethod
    def argument_names(cls) -> list[str]:
        return [f"commit_message={cls.default_message}"]

    @classmethod
    def help_message(cls) -> str:
        return "Commits all of your unstaged and staged changes to git"


class AddCommand(Command, command_name="add"):
    def __init__(self, code_context: CodeContext):
        self.code_context = code_context

    def apply(self, *args: str) -> None:
        if len(args) == 0:
            cprint("No files specified\n", "yellow")
            return
        for file_path in args:
            code_file = CodeFile(file_path)
            self.code_context.add_file(code_file)

    @classmethod
    def argument_names(cls) -> list[str]:
        return ["file1", "file2", "..."]

    @classmethod
    def help_message(cls) -> str:
        return "Add files to the code context"


class RemoveCommand(Command, command_name="remove"):
    def __init__(self, code_context: CodeContext):
        self.code_context = code_context

    def apply(self, *args: str) -> None:
        if len(args) == 0:
            cprint("No files specified\n", "yellow")
            return
        for file_path in args:
            code_file = CodeFile(file_path)
            self.code_context.remove_file(code_file)

    @classmethod
    def argument_names(cls) -> list[str]:
        return ["file1", "file2", "..."]

    @classmethod
    def help_message(cls) -> str:
        return "Remove files from the code context"
