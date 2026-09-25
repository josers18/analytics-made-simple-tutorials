# Grok prompt: verify a claim and cite the page

> **Official companion for [Learn Grok](https://analyticsmadesimple.com/series/grok/)**

This file is a prompt for a Grok chat that can search. Paste it. It does not search by itself.

A Python call to the xAI API, without search, is [`01_xai_api_client.py`](./01_xai_api_client.py).

## Paste this

```text
Check this claim against pages on duckdb.org. Use search.

Claim: "DuckDB 1.2 added window-function optimizations."

Reply with one label: CONFIRMED, REFUTED, or INCONCLUSIVE.
Then give two URLs you actually opened, and one sentence on what each page says.
If you cannot open a page, say so. Do not invent a URL.
```

## Next

[Imagine prompt](./04_grok_imagine_prompt_engineering.md)
