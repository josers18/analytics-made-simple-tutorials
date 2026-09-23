# ChatGPT Tutorial 3: Automated Code Reviews with Codex

> **Official Companion Guide for [Analytics Made Simple: ChatGPT Code Reviews](https://analyticsmadesimple.com/series/chatgpt/)**
> Raw Script: [`03_codex_automated_code_reviews.py`](./03_codex_automated_code_reviews.py)

Automate pull request verification by injecting git diffs into structured audit prompts that detect data grain violations, non-sargable queries, and division-by-zero risks.

---

## The Complete Python Script

Below is the code contained in [`03_codex_automated_code_reviews.py`](./03_codex_automated_code_reviews.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Automated Code Review and Test Generation
Series: ChatGPT Codex Tutorial
License: MIT
"""

def generate_code_review_prompt(diff_text: str) -> str:
    """Creates a targeted prompt auditing code changes for SQL & Python anti-patterns."""
    return f"""You are a senior data engineer performing a pull request review.

### Staged Git Diff:
```diff
{diff_text}
```

### Review Checklist:
1. Detect unverified data grain or potential 1:N join fan-out issues.
2. Flag non-sargable SQL filters (e.g. strftime() or LOWER() on indexed columns).
3. Check for unhandled NULLs in mathematical divisions.
4. Output your findings as a clean Markdown table with columns: [File, Severity, Issue, Suggested Fix].
"""

if __name__ == "__main__":
    mock_diff = """
--- a/queries/revenue.sql
+++ b/queries/revenue.sql
@@ -10,3 +10,4 @@
 SELECT customer_id, SUM(order_total) / COUNT(order_id)
 FROM orders
+WHERE strftime('%Y', order_date) = '2025'
 GROUP BY customer_id;
"""
    prompt = generate_code_review_prompt(mock_diff)
    print("=== Automated Code Review Prompt ===")
    print(prompt)
```

---

## Expected Review Table Output

When Codex evaluates the diff above, it produces:

| File | Severity | Issue | Suggested Fix |
|:---|:---|:---|:---|
| `queries/revenue.sql` | 🔴 High | Non-sargable date filter `strftime('%Y', order_date) = '2025'` | Replace with range: `order_date >= '2025-01-01' AND order_date < '2026-01-01'` |
| `queries/revenue.sql` | 🟡 Medium | Potential division by zero if `COUNT(order_id)` is 0 | Wrap with `NULLIF(COUNT(order_id), 0)` |

---

## How to Run

```bash
python3 chatgpt/03_codex_automated_code_reviews.py
```

👉 Next: [Part 4: Custom GPT Action OpenAPI Schema](./04_custom_gpt_action_openapi_schema.md)
