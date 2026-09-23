# Grok Tutorial 3: Real-Time Live Search & Verification

> **Official Companion Guide for [Analytics Made Simple: Grok Live Search](https://analyticsmadesimple.com/series/grok/)**
> Raw Script: [`03_grok_live_search_verification.py`](./03_grok_live_search_verification.py)

Leverage Grok's native live search integration to verify technical claims and extract timestamped primary sources.

---

## The Complete Python Script

Below is the code contained in [`03_grok_live_search_verification.py`](./03_grok_live_search_verification.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Real-Time Live Search & Verification with Grok
Series: Grok Everyday Tutorial
License: MIT
"""

def build_verification_prompt(claim: str, domain_filter: str) -> str:
    """Constructs a search prompt demanding live source citations."""
    return f"""You are a research verifier with real-time web search capabilities.

### Topic / Claim to Verify:
"{claim}"

### Verification Rules:
1. Search real-time sources within domain: {domain_filter}
2. Output a confidence assessment: [CONFIRMED, REFUTED, or INCONCLUSIVE].
3. Provide at least two direct citation URLs with timestamps.
4. Distinguish between official company releases and social speculation.
"""

if __name__ == "__main__":
    prompt = build_verification_prompt("DuckDB 1.2 release feature set and window function optimizations", "duckdb.org")
    print("=== Grok Live Verification Prompt ===")
    print(prompt)
```

---

## How to Run

```bash
python3 grok/03_grok_live_search_verification.py
```

👉 Next: [Part 4: Grok Imagine Visual Prompt Engineering](./04_grok_imagine_prompt_engineering.md)
