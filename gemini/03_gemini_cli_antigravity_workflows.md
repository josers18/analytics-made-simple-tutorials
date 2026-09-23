# Gemini Tutorial 3: Gemini CLI & Antigravity Workflows

> **Official Companion Guide for [Analytics Made Simple: Gemini CLI & Antigravity](https://analyticsmadesimple.com/series/gemini/)**
> Raw Script: [`03_gemini_cli_antigravity_workflows.sh`](./03_gemini_cli_antigravity_workflows.sh)

Master the 4-step developer cadence: **Ask → Edit → Test → Review**.

---

## The Complete Script

Below is the workflow setup contained in [`03_gemini_cli_antigravity_workflows.sh`](./03_gemini_cli_antigravity_workflows.sh):

```bash
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
```

---

## How to Run

```bash
bash gemini/03_gemini_cli_antigravity_workflows.sh
```

👉 Next: [Part 4: Google Sheets & Gemini Apps Script Automation](./04_gemini_workspace_sheets_automation.md)
