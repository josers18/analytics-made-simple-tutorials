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
