from llm_quality.providers.base import LLMProvider


class MockLLMProvider(LLMProvider):
    """Mock provider for local development and testing."""

    def generate(self, prompt: str) -> str:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        return f"Mock response for: {prompt}"
