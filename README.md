# Analytics Made Simple — Open-Source Code & Tutorials Companion

[![Website](https://img.shields.io/badge/Website-analyticsmadesimple.com-ff6600?style=flat-square)](https://analyticsmadesimple.com)
[![Substack](https://img.shields.io/badge/Substack-Subscribe%20Free-ff6600?style=flat-square&logo=substack)](https://analyticsmadesimple.substack.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-3776ab?style=flat-square&logo=python)](https://python.org)
[![SQL Dialects](https://img.shields.io/badge/SQL-SQLite%20%7C%20PostgreSQL%20%7C%20DuckDB-orange.svg?style=flat-square)](https://analyticsmadesimple.com/tutorials/)
[![Author](https://img.shields.io/badge/Author-Jose%20S-black?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/jsifontes)

Welcome to the official open-source companion repository for **[Analytics Made Simple](https://analyticsmadesimple.com)**.

This repository provides **runnable code, SQL queries, database schemas, interactive Jupyter notebooks, and workflow templates** corresponding to our published guides. Everything is engineered to be approachable for business practitioners and data analysts while remaining production-grade for software and analytics engineers.

---

## Repository Architecture

```text
analytics-made-simple-tutorials/
├── sql/                   # 14-Part SQL Mastery Curriculum (SQLite, PostgreSQL, DuckDB)
├── python/                # Python for Analytics: Pandas DataFrames, cleanup, grain verification
├── typesafe-ai/           # System One decision models, Jev implementations, RLCD logic
├── claude-code/           # Claude Code terminal workflows, developer prompts, and templates
└── ai-engineering/        # Prompt patterns for data work, LLM APIs, and vector search
```

---

## Learning Tracks Overview

### 1. [SQL Mastery Curriculum (`/sql`)](./sql/)
A progressive 14-part curriculum from relational database foundations to advanced analytics:
* **Interactive Notebook:** [`sql/sql_playground_interactive.ipynb`](./sql/sql_playground_interactive.ipynb)
* **Part 0:** [What is SQL and Why Learn It?](./sql/00_what_is_sql.md) · [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/what-is-sql/)
* **Part 1:** [Setting Up Your SQL Playground (`customers`, `orders`, `order_lines`)](./sql/01_playground_setup.md)
* **Part 2:** [Master the Core Commands (SELECT, INSERT, UPDATE, DELETE)](./sql/02_core_commands.md)
* **Part 3:** [Retrieving Data with SELECT & Aliases](./sql/03_select_queries.md)
* **Part 4:** [Filtering & Sorting (WHERE, IN, BETWEEN, LIKE, ORDER BY)](./sql/04_filtering_and_sorting.md)
* **Part 5:** [Aggregate Functions & Grouping (COUNT, SUM, GROUP BY, HAVING)](./sql/05_aggregates_grouping.md)
* **Part 6:** [Joins & Relationships (INNER, LEFT, FULL, preventing fan-out)](./sql/06_joins_and_relationships.md)
* **Part 7:** [Subqueries (Scalar, IN, Correlated, EXISTS)](./sql/07_subqueries.md)
* **Part 8:** [Modifying Data & ACID Transactions (BEGIN, COMMIT, ROLLBACK)](./sql/08_modifying_data_transactions.md)
* **Part 9:** [Views and B-Tree Indexes (CREATE VIEW, EXPLAIN plans)](./sql/09_views_and_indexes.md)
* **Part 10:** [Advanced SQL (CTEs, ROW_NUMBER, RANK, moving averages)](./sql/10_advanced_ctes_window_functions.md)
* **Part 11:** [Stored Procedures & Event Triggers](./sql/11_stored_procedures_triggers.md)
* **Part 12:** [Query Optimization & Sargability](./sql/12_optimization_and_explain.md)
* **Part 13:** [Database Maintenance (VACUUM, ANALYZE, integrity checks)](./sql/13_database_maintenance.md)

👉 [Browse SQL Scripts & Schemas ↗](./sql/)

---

### 2. [Python for Analytics & Data Engineering (`/python`)](./python/)
Production patterns for data manipulation, ETL pipelines, and stakeholder hand-offs:
* **Interactive Notebook:** [`python/pandas_analytics_cookbook.ipynb`](./python/pandas_analytics_cookbook.ipynb)
* **Setup:** [Environment Setup Without Tears (`venv`, pip, dependencies)](./python/01_environment_setup.md)
* **DataFrames:** [DataFrames as SQL Tables](./python/02_dataframes_as_tables.md)
* **Transformations:** [Selecting, Filtering, and Sorting in Pandas](./python/03_selecting_filtering_sorting.md)
* **Data Cleanup:** [Standardizing Categories and Messy Company Names](./python/04_standardizing_categories_and_names.md)
* **Integrity:** [Grain Verification Assertions & Parquet Export](./python/05_verify_grain_and_export.md)
* **Database Bridge:** [Connecting Python and SQL Together via SQLAlchemy](./python/06_python_and_sql_together.md)

👉 [Browse Python Scripts ↗](./python/)

---

### 3. [TypeSafe AI & System One Models (`/typesafe-ai`)](./typesafe-ai/)
High-speed (110ms), calibrated decision layers replacing brittle regular expressions and multi-second LLM loops:
* **Interactive Notebook:** [`typesafe-ai/typesafe_ai_decision_layer.ipynb`](./typesafe-ai/typesafe_ai_decision_layer.ipynb)
* **Customer Triage:** [110ms Calibrated Support & Refund Decision Engine](./typesafe-ai/01_customer_triage_engine.md) · [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/jev-typesafe-ai-system-one-model-rlcd-tutorial/)
* **Risk Routing:** [Two-Axis Confidence Gating for Financial Transactions](./typesafe-ai/02_sentiment_and_routing_pipeline.md)

👉 [Browse TypeSafe AI Code ↗](./typesafe-ai/)

---

### 4. [Claude Code & Agent Workflows (`/claude-code`)](./claude-code/)
Terminal-native agent engineering, instructions, and developer automations:
* **Terminal Setup:** [macOS, Linux, and Windows Installation & Authentication](./claude-code/01_terminal_setup_and_quickstart.md)
* **Instruction Templates:** [Production `CLAUDE.md` and `AGENTS.md` Configurations](./claude-code/02_instruction_templates/)
* **Automated Reviews:** [Pre-commit Agentic Code Review Script](./claude-code/03_automated_code_review_workflow.sh)
* **Analyst Workflows:** [Pair-Programming with Claude Code on Schema Audits & Data Tasks](./claude-code/04_data_analyst_agent_guide.md)

👉 [Browse Claude Code Workflows ↗](./claude-code/)

---

### 5. [AI Engineering: Prompts, APIs & Vector Search (`/ai-engineering`)](./ai-engineering/)
Core patterns for generative AI applications and retrieval systems:
* **Interactive Notebook:** [`ai-engineering/rag_and_vector_search.ipynb`](./ai-engineering/rag_and_vector_search.ipynb)
* **Prompt Patterns:** [Schema-Constrained System Prompts for Data Tasks](./ai-engineering/01_prompt_patterns_for_data.md)
* **Universal API Client:** [Unified Python Wrapper for OpenAI, Claude, and xAI](./ai-engineering/02_llm_api_unified_client.md)
* **Vector Search:** [Zero-Dependency Vector Similarity Search in Python + SQLite](./ai-engineering/03_vector_search_sqlite.md)

👉 [Browse AI Engineering Code ↗](./ai-engineering/)

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/josers18/analytics-made-simple-tutorials.git
cd analytics-made-simple-tutorials
```

### 2. Launch Interactive Notebooks
```bash
# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy sqlalchemy duckdb pyarrow jupyterlab matplotlib

# Launch JupyterLab
jupyter lab
```

### 3. Initialize the Practice SQL Database
```bash
sqlite3 ams_playground.db < sql/01_playground_setup.sql
```

---

## Stay Connected

* 🌐 **Main Publication:** [analyticsmadesimple.com](https://analyticsmadesimple.com)
* 📬 **Substack Newsletter:** [analyticsmadesimple.substack.com](https://analyticsmadesimple.substack.com)
* ⭐ **Google Preferred Source:** [Follow Analytics Made Simple on Google](https://www.google.com/preferences/source?q=analyticsmadesimple.com) to prioritize our guides in your Google Search and Discover feeds.
* 💼 **Author:** Jose S on [LinkedIn](https://www.linkedin.com/in/jsifontes) · GitHub [@josers18](https://github.com/josers18)

---

## License

This repository is licensed under the [MIT License](./LICENSE). All code, schemas, and queries are free to use in personal, educational, and commercial projects.
