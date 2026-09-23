# ChatGPT Tutorial 2: Codex Sandbox & Safe Repo Exploration

> **Official Companion Guide for [Analytics Made Simple: ChatGPT Codex Workflows](https://analyticsmadesimple.com/series/chatgpt/)**
> Raw Script: [`02_codex_sandbox_repo_exploration.sh`](./02_codex_sandbox_repo_exploration.sh)

Using agentic coding assistants like OpenAI Codex or Canvas requires establishing clear safety boundaries. Never point an agent directly at a dirty production clone.

---

## The Complete Setup Script

Below is the sandbox isolation script contained in [`02_codex_sandbox_repo_exploration.sh`](./02_codex_sandbox_repo_exploration.sh):

```bash
#!/usr/bin/env bash
# Analytics Made Simple (analyticsmadesimple.com)
# Tutorial: Exploring Repositories Safely with Codex / OpenAI Canvas
# Series: ChatGPT Codex Tutorial
# License: MIT

set -euo pipefail

echo "🛡️ Initializing Safe Practice Sandbox for Codex..."

SANDBOX_DIR="$HOME/sandbox/codex-first-run"
mkdir -p "$SANDBOX_DIR"
cd "$SANDBOX_DIR"

if [ ! -d ".git" ]; then
    git init
    echo "# Toy Analytics Warehouse" > README.md
    echo "order_id,amount,status" > orders.csv
    echo "101,450.00,completed" >> orders.csv
    git add .
    git commit -m "Initial commit for Codex practice"
    echo "✅ Sandbox repository created at $SANDBOX_DIR"
fi

# Create dedicated practice branch
git checkout -B practice/codex-exploration

echo "
📋 Recommended Safe Prompt Sequence for Codex:
1. Read-Only Query:
   'What does this project do and what is the primary schema in orders.csv?'
2. Targeted Single-File Edit:
   'In README.md only, add a data dictionary table documenting order_id, amount, and status.'
3. Review Diff:
   Run 'git diff' to inspect changes before committing!
"
```

---

## Safe AI Pair Programming Routine

```text
1. Sandbox Clone    -> Create clean git branch (git checkout -b practice/...)
2. Read-Only Prompt -> Ask architecture questions before requesting edits
3. Targeted Diff    -> Constrain edits to 1 file at a time
4. Human Review     -> Inspect 'git diff' and test before staging
```

---

## How to Run

```bash
bash chatgpt/02_codex_sandbox_repo_exploration.sh
```

👉 Next: [Part 3: Automated Code Reviews with Codex](./03_codex_automated_code_reviews.md)
