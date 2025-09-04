"""
Author: Louis Goodnews
Date: 2025-08-25
"""

from typing import Final, List, Literal

from .core.core import FileManager, FileTask


__all__: Final[List[str]] = [
    "FileManager",
    "FileTask",
]

__version__: Final[Literal["0.1.0"]] = "0.1.0"
