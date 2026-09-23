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

set -euo pipefail

echo "🔍 Running Automated Repository Health Check..."

# 1. Check for unstaged changes
if ! git diff --quiet; then
    echo "⚠️  Unstaged changes detected. Generating review diff..."
    git diff > /tmp/claude_review_diff.patch
    echo "✅ Diff saved to /tmp/claude_review_diff.patch"
fi

# 2. Invoke Claude Code in non-interactive review mode
echo "🤖 Triggering Claude Code review pass..."
claude --prompt "Please review the latest git changes for potential grain violations, missing SQL indexes, and unhandled null values. Provide concise, bulleted feedback."

echo "✅ Review complete!"
```

---

## How It Works

1. **Diff Extraction:** `DIFF=$(git diff HEAD)` extracts all staged and unstaged code changes.
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
