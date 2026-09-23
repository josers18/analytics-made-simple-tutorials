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
