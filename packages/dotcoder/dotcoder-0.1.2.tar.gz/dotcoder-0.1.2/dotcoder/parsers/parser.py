import logging
import signal
from abc import ABC, abstractmethod
from asyncio import Event
from contextlib import contextmanager
from types import FrameType
from typing import Any, AsyncGenerator

from dotcoder.code_file_manager import CodeFileManager
from dotcoder.config_manager import ConfigManager
from dotcoder.parsers.file_edit import FileEdit


class Parser(ABC):
    def __init__(self):
        self.shutdown = Event()

    def shutdown_handler(self, sig: int, frame: FrameType | None):
        print("\n\nInterrupted by user. Using the response up to this point.")
        logging.info("User interrupted response.")
        self.shutdown.set()

    # Interface redesign will likely completely change interrupt handling
    @contextmanager
    def interrupt_catcher(self):
        signal.signal(signal.SIGINT, self.shutdown_handler)
        yield
        # Reset to default interrupt handler
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.shutdown.clear()

    @abstractmethod
    def get_system_prompt(self) -> str:
        pass

    @abstractmethod
    async def stream_and_parse_llm_response(
        self,
        response: AsyncGenerator[Any, None],
        code_file_manager: CodeFileManager,
        config: ConfigManager,
    ) -> tuple[str, list[FileEdit]]:
        pass
