# Analytics Made Simple — Open-Source Code & Tutorials Companion

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Analytics Made Simple](https://img.shields.io/badge/Publication-Analytics%20Made%20Simple-orange.svg)](https://analyticsmadesimple.com)
[![Substack](https://img.shields.io/badge/Newsletter-Substack-ff6719.svg)](https://analyticsmadesimple.substack.com)

Welcome to the official open-source code and companion repository for **[Analytics Made Simple](https://analyticsmadesimple.com)**.

This repository provides **runnable code scripts**, **visual Markdown walkthroughs with embedded code**, and **interactive Jupyter notebooks** designed to help business and technical professionals master data analytics, relational databases, AI systems, and automated developer workflows.

---

## Architecture & Directory Overview

```text
analytics-made-simple-tutorials/
├── sql/                   # 14-Part SQL curriculum, schemas, and queries
├── python/                # Pandas data manipulation, typing, and grain checks
├── chatgpt/               # OpenAI ChatGPT, Codex sandboxes, and Custom GPTs
├── gemini/                # Google Gemini SDK, AI Studio, CLI & Workspace
├── grok/                  # xAI Grok REST API, Grok Build CLI & Imagine prompts
├── claude-code/           # Claude Code terminal agent workflows & prompts
├── typesafe-ai/           # System One decision models, Jev & low-latency triage
└── ai-engineering/        # Prompt patterns, unified LLM clients & vector search
```

---

## Curriculum Tracks

| Track | Focus & Core Skills | Primary Languages / Tools | Directory | Interactive Notebook | Live Publication Hub |
|:---|:---|:---:|:---:|:---:|:---:|
| **SQL Mastery** | Schemas, CRUD, joins, subqueries, transactions, indexes, CTEs & window functions | SQL, SQLite, DuckDB | [`/sql/`](./sql/) | [`sql_playground_interactive.ipynb`](./sql/sql_playground_interactive.ipynb) | [SQL Tutorials ↗](https://analyticsmadesimple.com/series/sql/) |
| **Python Analytics** | DataFrames, cleaning, string standardization, grain verification & Parquet export | Python, Pandas, PyArrow | [`/python/`](./python/) | [`pandas_analytics_cookbook.ipynb`](./python/pandas_analytics_cookbook.ipynb) | [Tutorials Hub ↗](https://analyticsmadesimple.com/tutorials/) |
| **ChatGPT & Codex** | Paste-ready prompts, a Codex sandbox, an example OpenAPI schema, and one OpenAI SDK call | Python, Bash, OpenAPI | [`/chatgpt/`](./chatgpt/) | [`chatgpt_data_analysis_cookbook.ipynb`](./chatgpt/chatgpt_data_analysis_cookbook.ipynb) | [ChatGPT Series ↗](https://analyticsmadesimple.com/series/chatgpt/) |
| **Gemini & Antigravity** | Google GenAI SDK, multimodal vision, Gemini CLI, and Sheets Apps Script | Python, Apps Script, Bash | [`/gemini/`](./gemini/) | [`gemini_long_context_analytics.ipynb`](./gemini/gemini_long_context_analytics.ipynb) | [Gemini Series ↗](https://analyticsmadesimple.com/series/gemini/) |
| **Grok & Grok Build** | xAI API, Grok Build terminal agent loop, live search, and Imagine prompts | Python, Bash, REST | [`/grok/`](./grok/) | [`grok_analytics_and_code_loop.ipynb`](./grok/grok_analytics_and_code_loop.ipynb) | [Grok Series ↗](https://analyticsmadesimple.com/series/grok/) |
| **Claude Code** | Terminal setup, CLAUDE.md instruction templates, pre-commit code review hooks | Bash, Markdown | [`/claude-code/`](./claude-code/) | — | [Claude Series ↗](https://analyticsmadesimple.com/series/claude/) |
| **TypeSafe AI** | System One calls through the TypeSafe SDK (`choices`, `scores`, `nouls`) | Python | [`/typesafe-ai/`](./typesafe-ai/) | [`typesafe_ai_decision_layer.ipynb`](./typesafe-ai/typesafe_ai_decision_layer.ipynb) | [Jev & System One ↗](https://analyticsmadesimple.com/tutorials/jev-typesafe-ai-system-one-model-rlcd-tutorial/) |
| **AI Engineering** | Constrained system prompts, unified multi-LLM API client, and SQLite vector search | Python, SQLite | [`/ai-engineering/`](./ai-engineering/) | [`rag_and_vector_search.ipynb`](./ai-engineering/rag_and_vector_search.ipynb) | [AI Tutorials ↗](https://analyticsmadesimple.com/tutorials/) |

---

## Quickstart

### 1. Run the SQL Playground Locally
SQLite is pre-installed on macOS and Linux. Execute the full database setup in one command:
```bash
sqlite3 ams_playground.db < sql/01_playground_setup.sql
sqlite3 ams_playground.db "SELECT * FROM customers;"
```

### 2. Run Python Analytics Scripts
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt   # or: pip install pandas numpy pyarrow

# Run data cleaning and grain verification
python3 python/04_standardizing_categories_and_names.py
python3 python/05_verify_grain_and_export.py
```

### 3. Launch Interactive Notebooks
```bash
pip install jupyterlab
jupyter lab
```

---

## About Analytics Made Simple

**Analytics Made Simple** publishes in-depth, publication-grade tutorials, architectural guides, and decision frameworks for data and business leaders.

* 🌐 **Main Publication:** [analyticsmadesimple.com](https://analyticsmadesimple.com)
* 📬 **Substack Newsletter:** [analyticsmadesimple.substack.com](https://analyticsmadesimple.substack.com)
* ⭐ **Google Preferred Source:** [Follow Analytics Made Simple on Google](https://www.google.com/preferences/source?q=analyticsmadesimple.com) to prioritize our guides in your Google Search and Discover feeds.
* 💼 **Author:** Jose S on [LinkedIn](https://www.linkedin.com/in/jsifontes) · GitHub [@josers18](https://github.com/josers18)

---

## License

This repository is licensed under the [MIT License](./LICENSE). All code, schemas, and queries are free to use in personal, educational, and commercial projects.
