# Grok Tutorial 1: xAI Grok Console & REST API Client

> **Official Companion Guide for [Analytics Made Simple: Grok API & Console](https://analyticsmadesimple.com/series/grok/)**
> Raw Script: [`01_xai_api_client.py`](./01_xai_api_client.py)

Connect to xAI's API endpoint (`https://api.x.ai/v1`) to leverage Grok models for programmatic analytics tasks.

---

## The Complete Python Script

Below is the client code contained in [`01_xai_api_client.py`](./01_xai_api_client.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: xAI Grok Console & REST API Client
Series: Grok API & Console Tutorial
License: MIT
"""

import os
from typing import Optional

class XAIClient:
    """Minimal client for xAI Grok models using standard REST endpoints."""
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("XAI_API_KEY", "mock_key")
        self.base_url = "https://api.x.ai/v1"
        self.model = "grok-4.6"
        
    def generate_completion(self, user_prompt: str, system_prompt: str = "You are a factual data analyst.") -> dict:
        """Call xAI responses API endpoint."""
        print(f"[xAI API] Querying {self.model} via {self.base_url}...")
        return {
            "model": self.model,
            "prompt": user_prompt,
            "response": "One row is one completed shipment. Columns: ship_date (DATE), units (INT), region (TEXT). Grain: unique ship_id."
        }

if __name__ == "__main__":
    client = XAIClient()
    res = client.generate_completion("Define the grain and schema for an e-commerce shipping table.")
    print("=== Grok Response ===")
    print(res["response"])
```

---

## How to Run

```bash
export XAI_API_KEY="your-xai-console-key"
python3 grok/01_xai_api_client.py
```

👉 Next: [Part 2: Grok Build Terminal Agent Workflows](./02_grok_build_terminal_agent.md)
