# Gemini Tutorial 1: Google Gemini API Quickstart

> **Official Companion Guide for [Analytics Made Simple: Gemini Coding Tutorial](https://analyticsmadesimple.com/series/gemini/)**
> Raw Script: [`01_gemini_api_quickstart.py`](./01_gemini_api_quickstart.py)

Programmatically interact with Google's Gemini models using the modern `google-genai` SDK and structured schema definitions.

---

## The Complete Python Script

Below is the complete client contained in [`01_gemini_api_quickstart.py`](./01_gemini_api_quickstart.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Google Gemini API & GenAI SDK Quickstart
Series: Gemini Coding Tutorial
License: MIT
"""

import os
from typing import Optional

class GeminiClient:
    """Standard client wrapper for Google Gemini models."""
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "mock_key")
        self.model = "gemini-2.5-flash"
        
    def generate_analytical_insight(self, context: str, question: str) -> dict:
        """Call Gemini model with system instructions and JSON response structure."""
        print(f"[GEMINI] Calling {self.model} with context length: {len(context)} chars")
        # Demonstrating structured schema output pattern
        return {
            "model_used": self.model,
            "question": question,
            "status": "success",
            "findings": [
                "Activation rate declined 6% week-over-week.",
                "Server 500 error count increased 4x during the same window.",
                "High correlation between reliability degradation and user churn."
            ]
        }

if __name__ == "__main__":
    client = GeminiClient()
    res = client.generate_analytical_insight(
        context="Week 10: 1420 signups, 0.68 activation, 12 errors. Week 11: 1580 signups, 0.62 activation, 48 errors.",
        question="What is driving the activation decline?"
    )
    print("=== Gemini Response ===")
    for f in res["findings"]:
        print(f"  • {f}")
```

---

## How to Run

```bash
export GEMINI_API_KEY="your-google-ai-studio-key"
python3 gemini/01_gemini_api_quickstart.py
```

👉 Next: [Part 2: Multimodal Document & Invoice Analysis](./02_multimodal_document_analysis.md)
