# AI Engineering: Unified LLM Client

> **Official Companion Guide for [Analytics Made Simple: Chat APIs](https://analyticsmadesimple.com/tutorials/)**
> Raw Script: [`02_llm_api_unified_client.py`](./02_llm_api_unified_client.py)

Learn how to structure multi-provider LLM integrations across OpenAI, Anthropic, and xAI with a uniform, interchangeable interface.

---

## The Complete Python Script

Below is the complete script contained in [`02_llm_api_unified_client.py`](./02_llm_api_unified_client.py):

```python
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
```

---

## Execution Output

```text
[OPENAI] Querying model with system: 'You are a helpful data assista...'
Mock response from openai for prompt: 'Explain grain in data modeling....'

[ANTHROPIC] Querying model with system: 'You are a helpful data assista...'
Mock response from anthropic for prompt: 'Explain grain in data modeling....'

[XAI] Querying model with system: 'You are a helpful data assista...'
Mock response from xai for prompt: 'Explain grain in data modeling....'
```

---

## How to Run

```bash
python3 ai-engineering/02_llm_api_unified_client.py
```

👉 Next: [Part 3: Vector Search from Scratch in SQLite](./03_vector_search_sqlite.md)
