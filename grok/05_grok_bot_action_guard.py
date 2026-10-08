"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Grok Bot tutorial: how to give xAI's AI coworker real work and keep it safe
https://analyticsmadesimple.com/tutorials/grokbot-from-zero-autonomous-digital-coworkers-xai-cursor/
License: MIT

Run:     python3 05_grok_bot_action_guard.py   (no key, no network, no installs)

The part of a self-built AI coworker that says no: a file path must stay inside the
working copy, and a command must be on an allow list. Everything else is refused.
"""

from pathlib import Path
import shlex

ALLOWED = {"git", "pytest", "ruff"}
BLOCKED_GIT = {"push", "reset", "clean"}


def inside(root, path):
    root = Path(root).resolve()
    target = (root / path).resolve()
    return target == root or root in target.parents


def command_ok(cmd):
    parts = shlex.split(cmd)
    if not parts or parts[0] not in ALLOWED:
        return False
    if parts[0] == "git" and len(parts) > 1 and parts[1] in BLOCKED_GIT:
        return False
    return True


root = "/tmp/worktrees/issue-1048"
for path in ["src/pricing.py", "../../etc/passwd"]:
    print(path, "->", "ok" if inside(root, path) else "blocked")
for cmd in ["pytest -q", "git push origin main", "rm -rf /"]:
    print(cmd, "->", "ok" if command_ok(cmd) else "blocked")
