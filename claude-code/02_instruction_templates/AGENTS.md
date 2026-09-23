# AGENTS.md — Multi-Agent Engineering Standards

> **Shared multi-agent conventions for Claude Code, Codex, Antigravity, and Grok.**

## Universal Rules
* **Git Cleanliness:** Always verify `git status` before and after modifying files. Never leave untracked scratch files in production trees.
* **Non-Destructive Operations:** Never run `DROP TABLE`, `rm -rf`, or database truncations without explicit confirmation.
* **Version Alignment:** When updating packages or themes, keep version numbers strictly synchronized across configuration files and documentation.
