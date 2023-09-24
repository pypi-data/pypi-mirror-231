from typing import Any, AsyncGenerator

from typing_extensions import override

from dotcoder.code_file_manager import CodeFileManager
from dotcoder.config_manager import ConfigManager
from dotcoder.parsers.file_edit import FileEdit
from dotcoder.parsers.original_format.original_format_parsing import (
    stream_and_parse_llm_response,
)
from dotcoder.parsers.parser import Parser
from dotcoder.prompts import block_parser_prompt


class BlockParser(Parser):
    @override
    def get_system_prompt(self) -> str:
        return block_parser_prompt

    @override
    async def stream_and_parse_llm_response(
        self,
        response: AsyncGenerator[Any, None],
        code_file_manager: CodeFileManager,
        config: ConfigManager,
    ) -> tuple[str, list[FileEdit]]:
        # Uses the legacy parsing code
        return await stream_and_parse_llm_response(
            response, code_file_manager, config, self.shutdown
        )
