from ._processor import Processor as Processor
from typing import Any

class Compiler:
    @staticmethod
    def load(path: str) -> dict[str, Any]: ...
    @classmethod
    def compile(cls, path: str, out_dir: str | None = ...) -> None: ...
