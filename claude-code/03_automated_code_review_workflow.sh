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
