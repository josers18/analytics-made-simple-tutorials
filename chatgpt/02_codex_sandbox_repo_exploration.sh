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
