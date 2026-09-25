# xAI API client

> **Official companion for [Learn Grok](https://analyticsmadesimple.com/series/grok/)**
> Raw script: [`01_xai_api_client.py`](./01_xai_api_client.py)

This script POSTs to `https://api.x.ai/v1/responses` with a bearer token. The model id defaults to `grok-4.7`. Set `XAI_MODEL` if that id has moved. The printed text is the body of the HTTP response.

## The script

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: xAI Grok REST API
https://analyticsmadesimple.com/series/grok/
License: MIT

Run: export XAI_API_KEY=... && python3 01_xai_api_client.py
Uses the documented Responses endpoint, https://api.x.ai/v1/responses, via the stdlib.
Override the model with XAI_MODEL if the default id has moved.
The script stops when the key is missing. It does not invent a reply.
"""

import json
import os
import sys
import urllib.error
import urllib.request


def response_text(payload: dict) -> str:
    if isinstance(payload.get("output_text"), str):
        return payload["output_text"]
    chunks = []
    for item in payload.get("output") or []:
        if not isinstance(item, dict):
            continue
        content = item.get("content")
        if isinstance(content, list):
            for part in content:
                if isinstance(part, dict) and part.get("text"):
                    chunks.append(part["text"])
        elif isinstance(item.get("text"), str):
            chunks.append(item["text"])
    if chunks:
        return "\n".join(chunks)
    try:
        return payload["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return json.dumps(payload, indent=2)


def main() -> None:
    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        sys.exit("Set XAI_API_KEY and run again.")
    model = os.environ.get("XAI_MODEL", "grok-4.7")
    body = json.dumps(
        {
            "model": model,
            "input": "In two sentences, define grain for an orders table. Do not invent column names beyond order_id.",
        }
    ).encode()
    request = urllib.request.Request(
        "https://api.x.ai/v1/responses",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        sys.exit(f"xAI API returned HTTP {exc.code}: {detail}")
    print(response_text(payload))


if __name__ == "__main__":
    main()
```

## How to run

```bash
export XAI_API_KEY=your_key
python3 01_xai_api_client.py
```

If the key or the SDK is missing, the script stops. It does not print a made-up answer.



## Next

[Grok Build shell notes](./02_grok_build_terminal_agent.md)
