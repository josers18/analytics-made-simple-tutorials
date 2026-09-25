"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: One question, three real APIs
License: MIT

Usage:
  export OPENAI_API_KEY=...    && python3 02_llm_api_unified_client.py openai
  export XAI_API_KEY=...       && python3 02_llm_api_unified_client.py xai
  export ANTHROPIC_API_KEY=... && python3 02_llm_api_unified_client.py anthropic

OpenAI and xAI use POST /v1/chat/completions. Anthropic uses POST /v1/messages.
Model ids default to the ids documented when this file was written. Override with
OPENAI_MODEL, XAI_MODEL, or ANTHROPIC_MODEL.
The script stops when the key for the provider you named is missing.
"""

import json
import os
import sys
import urllib.error
import urllib.request

PROVIDERS = {
    "openai": {
        "url": "https://api.openai.com/v1/chat/completions",
        "env": "OPENAI_API_KEY",
        "model_env": "OPENAI_MODEL",
        "model": "gpt-5.2",
        "style": "openai",
    },
    "xai": {
        "url": "https://api.x.ai/v1/chat/completions",
        "env": "XAI_API_KEY",
        "model_env": "XAI_MODEL",
        "model": "grok-4.7",
        "style": "openai",
    },
    "anthropic": {
        "url": "https://api.anthropic.com/v1/messages",
        "env": "ANTHROPIC_API_KEY",
        "model_env": "ANTHROPIC_MODEL",
        "model": "claude-sonnet-4-5",
        "style": "anthropic",
    },
}

QUESTION = "In two sentences, what does grain mean for an orders table?"


def post(url: str, headers: dict, payload: dict) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        sys.exit(f"HTTP {exc.code} from {url}: {detail}")


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in PROVIDERS:
        names = "|".join(PROVIDERS)
        sys.exit(f"Usage: python3 02_llm_api_unified_client.py {names}")
    spec = PROVIDERS[sys.argv[1]]
    api_key = os.environ.get(spec["env"])
    if not api_key:
        sys.exit(f"Set {spec['env']} and run again.")
    model = os.environ.get(spec["model_env"], spec["model"])
    if spec["style"] == "openai":
        payload = post(
            spec["url"],
            {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            {
                "model": model,
                "messages": [{"role": "user", "content": QUESTION}],
            },
        )
        print(payload["choices"][0]["message"]["content"])
        return
    payload = post(
        spec["url"],
        {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        {
            "model": model,
            "max_tokens": 300,
            "messages": [{"role": "user", "content": QUESTION}],
        },
    )
    print(payload["content"][0]["text"])


if __name__ == "__main__":
    main()
