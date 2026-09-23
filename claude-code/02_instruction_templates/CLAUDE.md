# CLAUDE.md — Data Analytics & Engineering Conventions

> **Production instruction template for Claude Code in data and analytics repositories.**

## Project Overview
* **Domain:** Core data analytics pipelines, SQL transformations, and metric calculations.
* **Stack:** Python 3.11+, pandas, DuckDB, PostgreSQL, dbt.

## Development & Test Commands
* Run unit tests: `pytest tests/`
* Format code: `black . && isort .`
* Lint checks: `ruff check .`
* Verify SQL syntax: `sqlfluff lint sql/`

## Coding Standards & Rules
1. **Grain Integrity:** Every analytical table or DataFrame transformation must document its primary grain in a top-level docstring.
2. **Deterministic Outputs:** Never rely on implicit sorting; always declare explicit `ORDER BY` clauses in analytical SQL and `.sort_values()` in pandas.
3. **No Unbounded Queries:** Never commit `SELECT *` without explicit column projection or a strict `LIMIT` clause in ad-hoc analysis.
4. **Error Handling:** Wrap all external database connections and filesystem exports in atomic transaction contexts.
