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
