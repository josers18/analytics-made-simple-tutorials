# A guard for an AI coworker: paths and commands

> **Official companion for [Grok Bot tutorial: how to give xAI's AI coworker real work and keep it safe](https://analyticsmadesimple.com/tutorials/grokbot-from-zero-autonomous-digital-coworkers-xai-cursor/)**
> Raw script: [`05_grok_bot_action_guard.py`](./05_grok_bot_action_guard.py)

Whether you use a hosted coworker like Grok Bot or wire up your own agent, the most important code is the part that says no. This script checks two things before an agent acts: that a file path stays inside its working copy (a Git worktree, a second folder on its own branch), and that a command is on an allow list. It runs on its own, with no AI service and no keys.

## The script

```python
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
```

## What each part does

1. **`ALLOWED`** lists the only programs the agent may run: `git`, `pytest` (runs the tests) and `ruff` (checks code style). **`BLOCKED_GIT`** lists the Git actions that publish or erase work: `push`, `reset`, `clean`.
2. **`inside(root, path)`** turns both paths into full locations with `resolve()`, which follows `..` steps. A path passes only if it is the working folder itself or somewhere under it, so `../../etc/passwd` (a system file two levels up) is refused.
3. **`command_ok(cmd)`** splits the command into words the way a shell would (`shlex.split`). The first word must be on the allow list, and a `git` command must not use a blocked action. Anything not listed is refused by default, which is safer than trying to list every dangerous command.
4. **The loops** run two paths and three commands through the checks and print the verdicts.

## Expected output

```text
src/pricing.py -> ok
../../etc/passwd -> blocked
pytest -q -> ok
git push origin main -> blocked
rm -rf / -> blocked
```

## How to run

```bash
python3 05_grok_bot_action_guard.py
```

Python 3.8 or newer, standard library only. To use it for real, call `inside()` and `command_ok()` before your agent writes a file or runs a command, and stop the action when either returns `False`. Pair it with GitHub branch protection so the bot's account cannot push to `main`.

## Next

- [Call the xAI API from Python](./01_xai_api_client.md)
- [Back to the Grok module](./README.md)
