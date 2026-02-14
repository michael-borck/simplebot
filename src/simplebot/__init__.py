"""SimpleBot - LLMs made simple for students and educators."""

from .core import get_response
from .personalities import (
    pirate_bot,
    shakespeare_bot,
    emoji_bot,
    teacher_bot,
    coder_bot,
)

__version__ = "0.1.0"

__all__ = [
    "get_response",
    "pirate_bot",
    "shakespeare_bot",
    "teacher_bot",
    "emoji_bot",
    "coder_bot",
]
