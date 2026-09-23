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
