#!/usr/bin/env bash
# Analytics Made Simple (analyticsmadesimple.com)
# Tutorial: Gemini CLI & Antigravity Loop (Ask -> Edit -> Test -> Review)
# Series: Gemini Coding Tutorial
# License: MIT

set -euo pipefail

echo "🤖 Initializing Gemini CLI & Antigravity Practice Environment..."

WORK_DIR="$HOME/sandbox/gemini-cli-practice"
mkdir -p "$WORK_DIR"
cd "$WORK_DIR"

if [ ! -d ".git" ]; then
    git init
    cat << 'EOF' > pipeline.py
def calculate_growth(prior, current):
    # Bug: Missing zero division check
    return (current - prior) / prior

print(calculate_growth(100, 150))
EOF
    git add pipeline.py
    git commit -m "add pipeline for gemini refactor"
fi

echo "
🔄 The 4-Step Antigravity Loop:
1. ASK:
   'gemini prompt "Explain the error in calculate_growth() in pipeline.py when prior is 0."'
2. EDIT:
   Let the agent make a focused, minimal change with safe guardrails.
3. TEST:
   Run unit tests locally (python3 pipeline.py).
4. REVIEW:
   Inspect git diff before committing!
"
