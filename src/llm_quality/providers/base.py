from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """Base contract for language model providers."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from a given prompt."""
        raise NotImplementedError
