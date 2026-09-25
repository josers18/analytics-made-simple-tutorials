"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Google Gemini API quickstart
https://analyticsmadesimple.com/series/gemini/
License: MIT

Install: pip install google-genai
Run:     export GEMINI_API_KEY=... && python3 01_gemini_api_quickstart.py
Override the model with GEMINI_MODEL if the default id has moved.
Official pattern: client.models.generate_content (Google GenAI SDK).
The script stops when the key or the SDK is missing. It does not invent a reply.
"""

import os
import sys


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Set GEMINI_API_KEY and run again.")
    try:
        from google import genai
    except ImportError:
        sys.exit("Install the SDK first: pip install google-genai")

    model = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents=(
            "Week 10: 1420 signups, activation 0.68, 12 server errors. "
            "Week 11: 1580 signups, activation 0.62, 48 server errors. "
            "In three sentences, what changed? Use only these numbers."
        ),
    )
    print(response.text)


if __name__ == "__main__":
    main()
