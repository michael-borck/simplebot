"""Pre-defined personality bots for SimpleBot."""

from .core import get_response
from typing import Optional

def pirate_bot(prompt: str, model: Optional[str] = None) -> str:
    """
    Generate a response in the style of a 1700s pirate with nautical slang.

    Args:
        prompt: The user's input text/question
        model: Optional model override

    Returns:
        A response written in pirate vernacular
    """
    return get_response(
        prompt,
        system="You are a witty pirate from the 1700s. "
               "Use nautical slang, say 'arr' occasionally, "
               "and reference sailing, treasure, and the sea.",
        model=model or "llama3"
    )

def shakespeare_bot(prompt: str, model: Optional[str] = None) -> str:
    """
    Generate a response in the style of William Shakespeare.

    Args:
        prompt: The user's input text/question
        model: Optional model override

    Returns:
        A response written in Shakespearean style
    """
    return get_response(
        prompt,
        system="You respond in the style of William Shakespeare, "
               "using Early Modern English vocabulary and phrasing.",
        model=model or "llama3"
    )

def emoji_bot(prompt: str, model: Optional[str] = None) -> str:
    """
    Generate a response primarily using emojis with minimal text.

    Args:
        prompt: The user's input text/question
        model: Optional model override

    Returns:
        A response composed primarily of emojis
    """
    return get_response(
        prompt,
        system="You respond using mostly emojis, mixing minimal words "
               "and symbols to convey meaning. You love using expressive "
               "emoji strings.",
        model=model or "llama3"
    )

def teacher_bot(prompt: str, model: Optional[str] = None) -> str:
    """
    Generate a response in the style of a patient, helpful educator.

    Args:
        prompt: The user's input text/question
        model: Optional model override

    Returns:
        A response with an educational approach
    """
    return get_response(
        prompt,
        system="You are a patient, encouraging teacher who explains "
               "concepts clearly at an appropriate level. Break down "
               "complex ideas into simpler components and use analogies "
               "when helpful.",
        model=model or "llama3"
    )

def coder_bot(prompt: str, model: Optional[str] = None) -> str:
    """
    Generate a response from a coding assistant optimized for programming help.

    Args:
        prompt: The user's input programming question or request
        model: Optional model override (defaults to a coding-specific model)

    Returns:
        A technical response focused on code-related assistance
    """
    return get_response(
        prompt,
        system="You are a skilled coding assistant who explains and writes "
               "code clearly and concisely. Prioritize best practices, "
               "readability, and proper error handling.",
        model=model or "codellama"
    )
