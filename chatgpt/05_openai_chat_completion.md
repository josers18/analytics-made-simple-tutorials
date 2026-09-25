# One OpenAI call that returns JSON

> **Official companion for [Learn ChatGPT](https://analyticsmadesimple.com/series/chatgpt/)**
> Raw script: [`05_openai_chat_completion.py`](./05_openai_chat_completion.py)

This script imports `openai`, sends two weeks of records, and asks for JSON with four keys: shipped, risks, key_metrics, recommended_action. The model id defaults to `gpt-5.2`. Set `OPENAI_MODEL` if that id has moved.

## The script

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: One real OpenAI chat call with a JSON schema
https://analyticsmadesimple.com/series/chatgpt/
License: MIT

Install: pip install openai
Run:     export OPENAI_API_KEY=... && python3 05_openai_chat_completion.py
Override the model with OPENAI_MODEL if the default id has moved.
The script stops when the key or the SDK is missing. It does not invent a reply.
"""

import json
import os
import sys

RECORDS = [
    {"week": "2025-W10", "signups": 1420, "activation_rate": 0.68, "server_errors": 12},
    {"week": "2025-W11", "signups": 1580, "activation_rate": 0.62, "server_errors": 48},
]

SYSTEM = """You are an analytics editor reviewing operational records.
Ground every claim in the input. If a number is not in the input, leave the list empty rather than inventing one.
Use short sentences."""

SCHEMA = {
    "type": "object",
    "properties": {
        "shipped": {"type": "array", "items": {"type": "string"}},
        "risks": {"type": "array", "items": {"type": "string"}},
        "key_metrics": {"type": "array", "items": {"type": "string"}},
        "recommended_action": {"type": "string"},
    },
    "required": ["shipped", "risks", "key_metrics", "recommended_action"],
    "additionalProperties": False,
}


def main() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("Set OPENAI_API_KEY and run again.")
    try:
        from openai import OpenAI
    except ImportError:
        sys.exit("Install the SDK first: pip install openai")

    model = os.environ.get("OPENAI_MODEL", "gpt-5.2")
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": "Summarize these weekly records:\n" + json.dumps(RECORDS),
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "analytics_summary",
                "strict": True,
                "schema": SCHEMA,
            },
        },
    )
    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
```

## How to run

```bash
pip install openai
export OPENAI_API_KEY=your_key
python3 05_openai_chat_completion.py
```

If the key or the SDK is missing, the script stops. It does not print a made-up answer.



## Next

[Prompt you can paste without Python](./01_chatgpt_prompt_patterns.md)
