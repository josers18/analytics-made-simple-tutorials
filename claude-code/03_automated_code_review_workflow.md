# Claude Code: Automated Pre-Commit Code Review Workflow

> **Official Companion Guide for [Analytics Made Simple: Claude Code Workflows](https://analyticsmadesimple.com/tutorials/)**
> Raw Script: [`03_automated_code_review_workflow.sh`](./03_automated_code_review_workflow.sh)

Integrate Claude Code directly into your local git developer lifecycle to review schema changes, SQL queries, and Python code before commits are created.

---

## The Complete Shell Script

Below is the complete bash review script contained in [`03_automated_code_review_workflow.sh`](./03_automated_code_review_workflow.sh):

```bash
#!/usr/bin/env bash
# Analytics Made Simple (analyticsmadesimple.com)
# Automated Code Review Workflow using Claude Code
# License: MIT
#
# Uses `claude -p` (non-interactive print mode). There is no --prompt flag.

set -euo pipefail

if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code is not on PATH. Install it, then run this script again."
  exit 1
fi

if git diff --quiet && git diff --cached --quiet; then
  echo "No unstaged or staged changes. Nothing to review."
  exit 0
fi

git diff HEAD > /tmp/claude_review_diff.patch
echo "Diff saved to /tmp/claude_review_diff.patch"

claude -p "Review the current git changes for grain violations, missing SQL indexes, and unhandled nulls. Use bullets. If none of those are in the diff, say so. Do not invent a finding."
```

---

## How It Works

1. **Diff extraction:** `git diff HEAD` writes staged and unstaged changes to `/tmp/claude_review_diff.patch`.
2. **Safety Check:** If no changes exist, the script terminates immediately with exit code 0.
3. **Headless Agent Invocation:** `claude -p "..."` runs Claude Code in headless prompt mode, injecting the exact diff into a specialized review prompt that checks for:
   * Non-sargable SQL functions (e.g. `strftime()` in `WHERE` clauses)
   * Missing foreign key indexes
   * DataFrame grain violations
   * Unhandled nulls or missing constraints

---

## How to Install as a Git Hook

```bash
# Copy into git hooks
cp claude-code/03_automated_code_review_workflow.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Now, every time you run `git commit`, Claude Code will automatically review your staged changes!

👉 Next: [Data Analyst Agent Guide](./04_data_analyst_agent_guide.md)
