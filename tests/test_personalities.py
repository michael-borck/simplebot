"""Tests for the SimpleBot personalities module."""

import pytest
from unittest.mock import patch
from simplebot import (
    pirate_bot,
    shakespeare_bot,
    emoji_bot,
    teacher_bot,
    coder_bot,
)

@patch("simplebot.personalities.get_response")
def test_pirate_bot(mock_get_response):
    """Test that pirate_bot calls get_response with correct parameters."""
    # Setup
    mock_get_response.return_value = "Arr, test response!"

    # Call function
    result = pirate_bot("Test prompt")

    # Assertions
    assert result == "Arr, test response!"
    mock_get_response.assert_called_once()
    # Check that system prompt contains pirate references
    system_arg = mock_get_response.call_args[1]["system"]
    assert "pirate" in system_arg.lower()

@patch("simplebot.personalities.get_response")
def test_custom_model(mock_get_response):
    """Test that personality bots accept custom model parameter."""
    # Setup
    mock_get_response.return_value = "Custom model response"

    # Call functions with custom model
    shakespeare_bot("Test", model="custom-model")

    # Assertions
    assert mock_get_response.call_args[1]["model"] == "custom-model"
