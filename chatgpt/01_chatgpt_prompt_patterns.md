# ChatGPT prompt: weekly records, no invented numbers

> **Official companion for [Learn ChatGPT](https://analyticsmadesimple.com/series/chatgpt/)**

This file is a prompt. Paste it into ChatGPT with the records under it. It does not call an API.

To send the same job through the OpenAI Python SDK, use [`05_openai_chat_completion.py`](./05_openai_chat_completion.py).

## Paste this

```text
You are an analytics editor reviewing operational records.

Ground every claim in the records below. If a number is not in the records, write UNKNOWN. Do not invent a cause.

Return four sections, in this order:
1) What changed
2) Risks
3) Key metrics (quote the numbers)
4) Recommended action

Records:
- 2025-W10: 1420 signups, activation rate 0.68, 12 server errors
- 2025-W11: 1580 signups, activation rate 0.62, 48 server errors
```

## What a useful answer looks like

The activation rate fell from 0.68 to 0.62 while server errors rose from 12 to 48. Signups rose from 1420 to 1580. The prompt does not say those two moves share a cause, so the answer should not invent one.

## Next

[Codex sandbox](./02_codex_sandbox_repo_exploration.md)
