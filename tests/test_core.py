"""Tests for the SimpleBot core module."""

import pytest
from unittest.mock import patch, MagicMock
from simplebot.core import get_response

@patch("simplebot.core.requests.post")
def test_successful_response(mock_post):
    """Test that a successful API response is handled correctly."""
    # Setup mock
    mock_response = MagicMock()
    mock_response.json.return_value = {"response": "Test response"}
    mock_post.return_value = mock_response

    # Call function
    result = get_response("Test prompt")

    # Assertions
    assert result == "Test response"
    mock_post.assert_called_once()

@patch("simplebot.core.requests.post")
def test_empty_prompt(mock_post):
    """Test that empty prompts are handled correctly."""
    result = get_response("")
    assert "Empty prompt" in result
    mock_post.assert_not_called()

@patch("simplebot.core.requests.post")
def test_api_error(mock_post):
    """Test that API errors are handled gracefully."""
    # Setup mock to raise an exception
    mock_post.side_effect = Exception("Test error")

    # Call function
    result = get_response("Test prompt")

    # Assertions
    assert "Error" in result
    assert "Test error" in result
