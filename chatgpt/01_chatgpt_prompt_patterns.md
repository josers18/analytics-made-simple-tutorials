# ChatGPT Tutorial 1: Structured Everyday Prompt Patterns

> **Official Companion Guide for [Analytics Made Simple: ChatGPT Everyday Workflows](https://analyticsmadesimple.com/series/chatgpt/)**
> Raw Script: [`01_chatgpt_prompt_patterns.py`](./01_chatgpt_prompt_patterns.py)

Moving beyond conversational chitchat to reliable analytical assistance requires disciplined prompt engineering: role constraints, explicit negative guardrails, and deterministic schema definitions.

---

## The Complete Python Script

Below is the complete prompt compiler contained in [`01_chatgpt_prompt_patterns.py`](./01_chatgpt_prompt_patterns.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: ChatGPT Everyday Prompt Patterns for Data Work
Series: Learn ChatGPT / Everyday Workflows
License: MIT
"""

import json
import os
from typing import Dict, Any

def generate_analytics_summary_prompt(data_records: list[dict], metric_goal: str) -> str:
    """
    Constructs a disciplined, few-shot prompt with strict guardrails
    banning invented numbers and enforcing structured JSON output.
    """
    return f"""You are an analytics editor reviewing operational records.

### Context:
Goal: {metric_goal}
Input Data:
{json.dumps(data_records, indent=2)}

### Strict Rules:
1. Ground every claim directly in the input data. Never invent metrics or extrapolate without stating assumptions.
2. Return ONLY valid JSON with keys: "shipped", "risks", "key_metrics", "recommended_action".
3. Use concise, active voice sentences.
"""

if __name__ == "__main__":
    sample_records = [
        {"week": "2025-W10", "signups": 1420, "activation_rate": 0.68, "server_errors": 12},
        {"week": "2025-W11", "signups": 1580, "activation_rate": 0.62, "server_errors": 48}
    ]
    prompt = generate_analytics_summary_prompt(sample_records, "Identify activation and reliability trends")
    print("=== Compiled ChatGPT Prompt ===")
    print(prompt)
```

---

## Key Prompt Components

1. **Delimited Context:** Data is wrapped in clear JSON blocks, preventing the model from confusing instruction text with user payload.
2. **Negative Constraints:** Explicitly commanding `"Never invent metrics"` dramatically suppresses hallucinated numbers.
3. **Structured Schema Output:** Demanding `"Return ONLY valid JSON"` allows downstream automation scripts to parse the model output safely.

---

## How to Run

```bash
python3 chatgpt/01_chatgpt_prompt_patterns.py
```

👉 Next: [Part 2: Codex Sandbox & Safe Repo Exploration](./02_codex_sandbox_repo_exploration.md)
