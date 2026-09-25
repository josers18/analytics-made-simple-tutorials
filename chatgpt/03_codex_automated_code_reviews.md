# Codex prompt: review a diff for grain and sargability

> **Official companion for [Learn ChatGPT](https://analyticsmadesimple.com/series/chatgpt/)**

This file is a prompt. Paste it into Codex or ChatGPT with a real diff under it. It does not review code by itself.

## Paste this

```text
You are reviewing a pull request for an analytics repo.

Check only the diff below.
1. Flag a join that can multiply rows before a SUM or COUNT.
2. Flag a filter that wraps an indexed column in a function, such as strftime() or LOWER().
3. Flag a division that can hit zero or NULL.
4. Reply as a markdown table with columns: File, Severity, Issue, Suggested fix.
If the diff does not contain one of those problems, say so. Do not invent a finding.

Diff:
--- a/queries/revenue.sql
+++ b/queries/revenue.sql
@@
 SELECT customer_id, SUM(order_total) / COUNT(order_id)
 FROM orders
+WHERE strftime('%Y', order_date) = '2025'
 GROUP BY customer_id;
```

The added filter calls `strftime` on `order_date`. That is the finding. A sargable form compares the column to a range, such as `order_date >= '2025-01-01' AND order_date < '2026-01-01'`.

## Next

[Custom GPT action schema](./04_custom_gpt_action_openapi_schema.md)
