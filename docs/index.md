# SimpleBot Documentation

> LLMs made simple for students and educators

SimpleBot is a lightweight Python wrapper that simplifies interactions with Large Language Models (LLMs) for educational settings. It abstracts away the complexity of API calls, model management, and error handling, allowing students to focus on learning programming concepts through engaging AI interactions.

## Installation

```bash
pip install simplebot
```

## Basic Usage

```python
from simplebot import get_response

# Basic usage with default model
response = get_response("Tell me about planets")
print(response)
```

## Personality Bots

SimpleBot comes with several pre-defined personality bots:

```python
from simplebot import pirate_bot, shakespeare_bot, emoji_bot, teacher_bot, coder_bot

# Get a response in pirate speak
pirate_response = pirate_bot("Tell me about sailing ships")
print(pirate_response)

# Get a response in Shakespearean style
shakespeare_response = shakespeare_bot("What is love?")
print(shakespeare_response)

# Get a response with emojis
emoji_response = emoji_bot("Explain happiness")
print(emoji_response)

# Get an educational response
teacher_response = teacher_bot("How do photosynthesis work?")
print(teacher_response)

# Get coding help
code_response = coder_bot("Write a Python function to check if a string is a palindrome")
print(code_response)
```

## API Reference

### get_response()

```python
def get_response(
    prompt: str,
    model: str = "llama3",
    system: str = "You are a helpful assistant.",
    stream: bool = False,
    api_url: Optional[str] = None,
) -> str:
```

The core function for sending prompts to an LLM and getting responses.

#### Parameters:

- `prompt`: The text prompt to send to the language model
- `model`: The name of the model to use (default: "llama3")
- `system`: System instructions that control the model's behavior
- `stream`: Whether to stream the response (default: False)
- `api_url`: Custom API URL (defaults to local Ollama server)

#### Returns:

- A string containing the model's response or an error message
