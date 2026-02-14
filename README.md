# SimpleBot

> LLMs made simple for students and educators

SimpleBot is a lightweight Python wrapper that simplifies interactions with Large Language Models (LLMs) for educational settings.

## Installation

```bash
pip install simplebot
```

## Quick Start

```python
from simplebot import get_response, pirate_bot

# Basic usage
response = get_response("Tell me about planets")
print(response)

# Use a personality bot
pirate_response = pirate_bot("Tell me about sailing ships")
print(pirate_response)
```

## About

This project is the case study from [Ship Python, Orchestrate AI: Professional Python in the AI Era](https://michael-borck.github.io/ship-python-orchestrate-ai), a book about professional Python development practices.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
