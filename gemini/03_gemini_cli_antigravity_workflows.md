# Gemini Tutorial 3: Gemini CLI & Antigravity Workflows

> **Official Companion Guide for [Analytics Made Simple: Gemini CLI & Antigravity](https://analyticsmadesimple.com/series/gemini/)**
> Raw Script: [`03_gemini_cli_antigravity_workflows.sh`](./03_gemini_cli_antigravity_workflows.sh)

This script builds a one-file practice repo and shows the division-by-zero error. It then prints the real `agy -p` command. It does not call the model for you.

---

## The Complete Script

Below is the workflow setup contained in [`03_gemini_cli_antigravity_workflows.sh`](./03_gemini_cli_antigravity_workflows.sh):

```bash
#!/usr/bin/env bash
# Analytics Made Simple (analyticsmadesimple.com)
# Tutorial: a tiny repo for Antigravity CLI (agy) or Gemini CLI
# Series: Gemini Coding Tutorial
# License: MIT
#
# The one-off prompt flag is -p. There is no "gemini prompt" subcommand.
# For individual accounts the current terminal binary is agy.

set -euo pipefail

WORK_DIR="${HOME}/sandbox/gemini-cli-practice"
mkdir -p "$WORK_DIR"
cd "$WORK_DIR"

if [ ! -d .git ]; then
  git init
  cat > pipeline.py << 'PY'
def calculate_growth(prior, current):
    return (current - prior) / prior


if __name__ == "__main__":
    print("100 to 150:", calculate_growth(100, 150))
    print("0 to 10:", calculate_growth(0, 10))
PY
  git add pipeline.py
  git commit -m "add pipeline with an unguarded division"
fi

echo "Practice repo: ${WORK_DIR}"
echo "The second call divides by zero, so Python stops:"
set +e
python3 pipeline.py
status=$?
set -e
echo "python3 exited ${status}"

cat << 'EOF'

Ask Antigravity CLI from this folder. The binary is agy:

  agy -p "In pipeline.py, calculate_growth divides by prior. When prior is 0 that raises ZeroDivisionError. Guard that case. Keep the 100 to 150 result."

gemini -p is the same shape if Gemini CLI is still signed in with an API key.

Then run:

  python3 pipeline.py
  git diff
EOF
```

---

## How to Run

```bash
bash gemini/03_gemini_cli_antigravity_workflows.sh
```

👉 Next: [Part 4: Google Sheets & Gemini Apps Script Automation](./04_gemini_workspace_sheets_automation.md)
