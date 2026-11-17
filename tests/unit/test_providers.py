import pytest

from llm_quality.providers.mock import MockLLMProvider


def test_mock_provider_returns_expected_response():
    provider = MockLLMProvider()

    response = provider.generate("What is artificial intelligence?")

    assert response == (
        "Mock response for: What is artificial intelligence?"
    )


def test_mock_provider_rejects_empty_prompt():
    provider = MockLLMProvider()

    with pytest.raises(ValueError, match="Prompt cannot be empty."):
        provider.generate("")


def test_mock_provider_rejects_whitespace_prompt():
    provider = MockLLMProvider()

    with pytest.raises(ValueError, match="Prompt cannot be empty."):
        provider.generate("   ")
