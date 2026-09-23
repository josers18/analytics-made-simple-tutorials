"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Universal LLM API Client (OpenAI, Claude, xAI)
License: MIT
"""

import os
from typing import Optional

class SimpleLLMClient:
    """Minimal unified client wrapper for commercial LLM APIs."""
    def __init__(self, provider: str = "openai", api_key: Optional[str] = None):
        self.provider = provider.lower()
        self.api_key = api_key or os.getenv(f"{self.provider.upper()}_API_KEY", "mock_key")
        
    def generate(self, prompt: str, system_prompt: str = "You are a helpful data assistant.") -> str:
        """Simulate or call the corresponding API endpoint."""
        print(f"[{self.provider.upper()}] Querying model with system: '{system_prompt[:30]}...'")
        return f"Mock response from {self.provider} for prompt: '{prompt[:40]}...'"

if __name__ == "__main__":
    for p in ["openai", "anthropic", "xai"]:
        client = SimpleLLMClient(provider=p)
        print(client.generate("Explain grain in data modeling."))
