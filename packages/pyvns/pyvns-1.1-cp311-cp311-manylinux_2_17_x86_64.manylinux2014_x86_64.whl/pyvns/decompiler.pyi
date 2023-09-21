from .content import ContentManager as ContentManager
from .naming import Naming as Naming
from typing import Any

class Decompiler:
    @classmethod
    def decompile(cls, _data: dict[str, dict[str, dict[str, Any]]], out: str) -> None: ...
