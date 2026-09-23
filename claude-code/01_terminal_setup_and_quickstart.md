# Claude Code: Terminal Setup & Quickstart

> **Official Companion Guide for [Analytics Made Simple: Install / Open Claude Code](https://analyticsmadesimple.com/tutorials/)**

Claude Code is Anthropic's official agentic command-line interface that lives directly inside your terminal, understands your Git repositories, and writes, debugs, and refactors code autonomously.

---

## 1. Installation

### macOS (Homebrew or Script)
```bash
# Recommended via Homebrew
brew install --cask claude-code

# Or native installer
curl -fsSL https://claude.ai/install.sh | bash
```

### Linux
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows (PowerShell)
```powershell
irm https://claude.ai/install.ps1 | iex
```

---

## 2. Authentication & First Run

Navigate to any Git repository and launch the CLI:
```bash
cd /path/to/your/project
claude
```
On first execution, Claude Code will open an OAuth browser window to link your Anthropic account.

---

## 3. Essential Keyboard Shortcuts & Commands

| Command | Action |
|---|---|
| `/help` | Display interactive CLI help menu |
| `/cost` | View token usage and session expenses |
| `/clear` | Reset context memory for a fresh conversation |
| `/compact` | Summarize trajectory to preserve context window |
| `Ctrl+C` | Cancel the current running model stream |
| `Ctrl+D` | Exit the Claude Code CLI |
