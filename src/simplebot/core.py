"""Core functionality for SimpleBot."""

import requests
import random
import time
from typing import Optional, Dict, Any

# Cache for the last used model to avoid redundant loading messages
_last_model: Optional[str] = None

def get_response(
    prompt: str,
    model: str = "llama3",
    system: str = "You are a helpful assistant.",
    stream: bool = False,
    api_url: Optional[str] = None,
) -> str:
    """
    Send a prompt to the LLM API and retrieve the model's response.

    Args:
        prompt: The text prompt to send to the language model
        model: The name of the model to use
        system: System instructions that control the model's behavior
        stream: Whether to stream the response
        api_url: Custom API URL (defaults to local Ollama server)

    Returns:
        The model's response text, or an error message if the request fails
    """
    global _last_model

    # Default to local Ollama if no API URL is provided
    if api_url is None:
        api_url = "http://localhost:11434/api/generate"

    # Handle model switching with friendly messages
    if model != _last_model:
        warmup_messages = [
            f"Loading model '{model}' into RAM... give me a sec...",
            f"Spinning up the AI core for '{model}'...",
            f"Summoning the knowledge spirits... '{model}' booting...",
            f"Thinking really hard with '{model}'...",
            f"Switching to model: {model} ... (may take a few seconds)",
        ]
        print(random.choice(warmup_messages))

        # Short pause to simulate/allow for model loading
        time.sleep(1.5)
        _last_model = model

    # Validate input
    if not prompt.strip():
        return "Empty prompt."

    # Prepare the request payload
    payload: Dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "system": system,
        "stream": stream
    }

    try:
        # Send request to the LLM API
        response = requests.post(
            api_url,
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response from model.")
    except requests.RequestException as e:
        return f"Connection Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
