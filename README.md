# SimpleBot

<!-- BADGES:START -->
[![case-study](https://img.shields.io/badge/-case--study-blue?style=flat-square)](https://github.com/topics/case-study) [![cli-tool](https://img.shields.io/badge/-cli--tool-blue?style=flat-square)](https://github.com/topics/cli-tool) [![educational-tools](https://img.shields.io/badge/-educational--tools-blue?style=flat-square)](https://github.com/topics/educational-tools) [![language-models](https://img.shields.io/badge/-language--models-blue?style=flat-square)](https://github.com/topics/language-models) [![machine-learning](https://img.shields.io/badge/-machine--learning-ff6f00?style=flat-square)](https://github.com/topics/machine-learning) [![natural-language-processing](https://img.shields.io/badge/-natural--language--processing-blue?style=flat-square)](https://github.com/topics/natural-language-processing) [![python](https://img.shields.io/badge/-python-3776ab?style=flat-square)](https://github.com/topics/python) [![wrapper](https://img.shields.io/badge/-wrapper-blue?style=flat-square)](https://github.com/topics/wrapper)
<!-- BADGES:END -->

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
