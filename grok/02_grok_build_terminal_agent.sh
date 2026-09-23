#!/usr/bin/env bash
# Analytics Made Simple (analyticsmadesimple.com)
# Tutorial: Grok Build CLI & Terminal Agent Workflows
# Series: Grok Build Tutorial
# License: MIT

set -euo pipefail

echo "⚡ Initializing Grok Build Practice Sandbox..."

SANDBOX_DIR="$HOME/sandbox/grok-build-toy"
mkdir -p "$SANDBOX_DIR"
cd "$SANDBOX_DIR"

if [ ! -d ".git" ]; then
    git init
    cat << 'EOF' > parse_dates.py
# Toy date parser with formatting defect
def parse_meetup_date(raw_str):
    # Expects "YYYY-MM-DD"
    parts = raw_str.split("-")
    return {"year": int(parts[0]), "month": int(parts[1]), "day": int(parts[2])}

print(parse_meetup_date("2025-03-25"))
EOF
    git add parse_dates.py
    git commit -m "start toy sandbox for Grok Build"
fi

echo "
🛠️ Grok Build Workflow Rules:
1. EXPLORE:
   Ask a read-only question first: 'Where are dates parsed and what happens if a month has 1 digit?'
2. CHANGE:
   Instruct Grok Build to make one minimal fix: 'Make parse_meetup_date robust to MM/DD/YYYY strings.'
3. CHECK:
   Run git diff to inspect the change before accepting!
"
