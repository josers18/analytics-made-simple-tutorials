# SQL Mastery Curriculum

Companion SQL scripts and playground datasets for the 14-part [SQL Series on Analytics Made Simple](https://analyticsmadesimple.com/series/sql/).

All scripts are written to run on standard relational databases (**SQLite**, **PostgreSQL**, or **DuckDB**) without proprietary lock-in.

---

## Curriculum Map

| Part | Title | Script | Tutorial Link |
|------|-------|--------|---------------|
| **00** | What is SQL? | Conceptual Overview | [Read Tutorial](https://analyticsmadesimple.com/tutorials/what-is-sql/) |
| **01** | Setting Up a Playground | [`01_playground_setup.sql`](./01_playground_setup.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/tutorial-1-setting-up-sql/) |
| **02** | Core Commands & Verbs | [`02_core_verbs.sql`](./02_core_verbs.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-2-core-commands/) |
| **03** | SELECT & Precise Questions | [`03_select_queries.sql`](./03_select_queries.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-3-select/) |
| **04** | Filtering and Sorting Data | [`04_filtering_sorting.sql`](./04_filtering_sorting.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-4-filter-sort/) |
| **05** | Aggregates and GROUP BY | [`05_aggregates_grouping.sql`](./05_aggregates_grouping.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-5-aggr-grouping/) |
| **06** | Joins & Entity Relationships | [`06_joins.sql`](./06_joins.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-6-joins-in-sql/) |
| **07** | Subqueries in SQL | [`07_subqueries.sql`](./07_subqueries.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-7-subqueries/) |
| **08** | Modifying Data & Transactions | [`08_modifying_data_transactions.sql`](./08_modifying_data_transactions.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-8-modifying-data-with-sql/) |
| **09** | Views and Indexes | [`09_views_indexes.sql`](./09_views_indexes.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-9-views-and-indexes/) |
| **10** | Window Functions and CTEs | [`10_window_functions_ctes.sql`](./10_window_functions_ctes.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-10-advanced-sql-techniques/) |
| **11** | Stored Procedures & Triggers | [`11_stored_procedures_triggers.sql`](./11_stored_procedures_triggers.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-11-stored-procedures-triggers-and-user-defined-functions/) |
| **12** | Best Practices & EXPLAIN | [`12_optimization_explain.sql`](./12_optimization_explain.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-12-best-practices-and-optimization/) |
| **13** | Maintenance & Reliability | [`13_maintenance_runbook.sql`](./13_maintenance_runbook.sql) | [Read Tutorial](https://analyticsmadesimple.com/tutorials/sql-tutorial-13-strategies-for-maintenance-and-optimization/) |

---

## How to Run Locally

You can run any of these scripts immediately using SQLite or DuckDB:

```bash
# Option A: SQLite (Pre-installed on macOS/Linux)
sqlite3 playground.db < 01_playground_setup.sql
sqlite3 playground.db < 03_select_queries.sql

# Option B: DuckDB
duckdb playground.duckdb < 01_playground_setup.sql
```
