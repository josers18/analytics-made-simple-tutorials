# SQL Mastery Curriculum

[![Curriculum](https://img.shields.io/badge/Track-SQL%20Mastery-blue.svg?style=flat-square)](https://analyticsmadesimple.com/tutorials/)
[![Dialects](https://img.shields.io/badge/Dialects-SQLite%20%7C%20PostgreSQL%20%7C%20DuckDB-orange.svg?style=flat-square)](https://analyticsmadesimple.com)
[![Interactive Notebook](https://img.shields.io/badge/Jupyter-Interactive%20Playground-green.svg?style=flat-square)](./sql_playground_interactive.ipynb)

Welcome to the official SQL Mastery curriculum companion for [Analytics Made Simple](https://analyticsmadesimple.com). This directory contains all SQL scripts, DDL schemas, test queries, and walkthrough documentation corresponding to our 14-part SQL series.

---

## Curriculum Index

| Part | Topic | Scripts | Walkthrough Guide | Live Article |
|:---:|:---|:---:|:---:|:---:|
| **0** | **What is SQL?** | — | [00_what_is_sql.md](./00_what_is_sql.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/what-is-sql/) |
| **1** | **Playground Setup** | [`01_playground_setup.sql`](./01_playground_setup.sql) | [01_playground_setup.md](./01_playground_setup.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/tutorial-1-setting-up-sql/) |
| **2** | **Core Commands** | [`02_core_commands.sql`](./02_core_commands.sql) | [02_core_commands.md](./02_core_commands.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-2-core-commands/) |
| **3** | **Retrieving Data (SELECT)** | [`03_select_queries.sql`](./03_select_queries.sql) | [03_select_queries.md](./03_select_queries.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-3-select/) |
| **4** | **Filtering & Sorting** | [`04_filtering_and_sorting.sql`](./04_filtering_and_sorting.sql) | [04_filtering_and_sorting.md](./04_filtering_and_sorting.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-4-filter-sort/) |
| **5** | **Aggregates & GROUP BY** | [`05_aggregates_grouping.sql`](./05_aggregates_grouping.sql) | [05_aggregates_grouping.md](./05_aggregates_grouping.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-5-aggr-grouping/) |
| **6** | **Joins & Entity Relations** | [`06_joins_and_relationships.sql`](./06_joins_and_relationships.sql) | [06_joins_and_relationships.md](./06_joins_and_relationships.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-6-joins-in-sql/) |
| **7** | **Subqueries** | [`07_subqueries.sql`](./07_subqueries.sql) | [07_subqueries.md](./07_subqueries.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-7-subqueries/) |
| **8** | **Modifying Data & Transactions** | [`08_modifying_data_transactions.sql`](./08_modifying_data_transactions.sql) | [08_modifying_data_transactions.md](./08_modifying_data_transactions.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-8-modifying-data-with-sql/) |
| **9** | **Views and Indexes** | [`09_views_and_indexes.sql`](./09_views_and_indexes.sql) | [09_views_and_indexes.md](./09_views_and_indexes.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-9-views-and-indexes/) |
| **10** | **Advanced SQL (CTEs & Windows)** | [`10_advanced_ctes_window_functions.sql`](./10_advanced_ctes_window_functions.sql) | [10_advanced_ctes_window_functions.md](./10_advanced_ctes_window_functions.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-10-advanced-sql-techniques/) |
| **11** | **Stored Procedures & Triggers** | [`11_stored_procedures_triggers.sql`](./11_stored_procedures_triggers.sql) | [11_stored_procedures_triggers.md](./11_stored_procedures_triggers.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-11-stored-procedures-triggers-and-user-defined-functions/) |
| **12** | **Optimization & EXPLAIN** | [`12_optimization_and_explain.sql`](./12_optimization_and_explain.sql) | [12_optimization_and_explain.md](./12_optimization_and_explain.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-12-best-practices-and-optimization/) |
| **13** | **Maintenance & Growth** | [`13_database_maintenance.sql`](./13_database_maintenance.sql) | [13_database_maintenance.md](./13_database_maintenance.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/sql-tutorial-13-strategies-for-maintenance-and-optimization/) |

---

## Quickstart

### Option A: Interactive Jupyter Notebook (Recommended)
Open [`sql_playground_interactive.ipynb`](./sql_playground_interactive.ipynb) directly in VS Code, JupyterLab, or Google Colab to execute queries with instant tabular output.

### Option B: SQLite CLI
```bash
# Initialize database
sqlite3 ams_playground.db < sql/01_playground_setup.sql

# Run any lesson
sqlite3 ams_playground.db < sql/06_joins_and_relationships.sql
```

### Option C: DuckDB
```bash
duckdb -c ".read sql/01_playground_setup.sql" -c ".read sql/10_advanced_ctes_window_functions.sql"
```
