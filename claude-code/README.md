# Claude Code & Developer Workflows

[![Track](https://img.shields.io/badge/Track-Claude%20Code-purple.svg?style=flat-square)](https://analyticsmadesimple.com/tutorials/)
[![Anthropic](https://img.shields.io/badge/CLI-Claude%20Code-black.svg?style=flat-square&logo=anthropic)](https://claude.ai)

Official open-source companion for the Claude Code and terminal agent engineering curriculum on [Analytics Made Simple](https://analyticsmadesimple.com).

---

## What's Inside

| Resource | Description | Path |
|:---|:---|:---:|
| **Terminal Setup & Quickstart** | macOS, Linux, and Windows installation, authentication, and core shortcuts | [01_terminal_setup_and_quickstart.md](./01_terminal_setup_and_quickstart.md) |
| **Instruction Templates** | Production `CLAUDE.md` and `AGENTS.md` configuration files for analytics | [`02_instruction_templates/`](./02_instruction_templates/) |
| **Automated Review Workflow** | Shell script executing automated pre-commit code reviews | [`03_automated_code_review_workflow.sh`](./03_automated_code_review_workflow.sh) · [Guide](./03_automated_code_review_workflow.md) |
| **Data Analyst Agent Guide** | Workflows for schema audits, SQL-to-Python translation, and documentation | [04_data_analyst_agent_guide.md](./04_data_analyst_agent_guide.md) |

---

## Quickstart

```bash
# 1. Install Claude Code (macOS)
brew install --cask claude-code

# 2. Copy production instructions to your repository root
cp claude-code/02_instruction_templates/CLAUDE.md ./CLAUDE.md

# 3. Launch the agent
claude
```
