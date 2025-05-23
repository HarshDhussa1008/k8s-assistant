from typing import Any
from abc import ABC, abstractmethod
    

class LLM(ABC):
    
    @abstractmethod
    def _initialize_client(self) -> Any:
        """Initialize and return the LLM client."""
        pass
    
    @abstractmethod
    def get_response(self, max_tokens: int, model: str, prompt: str, tools: list=[]) -> dict:
        """Get a response from the LLM model."""
        pass
    
    @abstractmethod
    def update_llm_history(self, role: str, content: str|list) -> None:
        """Update the user history with the latest user input."""
        pass
    
    def get_api_key(self) -> str:
        """Get the API key for the LLM."""
        return self.api_key
