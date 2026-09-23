# SQL Tutorial 2: Master the Core Commands

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 2 - Core Commands](https://analyticsmadesimple.com/tutorials/sql-tutorial-2-core-commands/)**

The four fundamental verbs of SQL are **SELECT**, **INSERT**, **UPDATE**, and **DELETE** (CRUD operations).

## Key Patterns
* Always use explicit column projections in production `SELECT` queries rather than `SELECT *`.
* Always test `WHERE` clauses on a `SELECT` before running `UPDATE` or `DELETE` to prevent accidental mass modifications.

👉 Run queries: `sqlite3 ams_playground.db < sql/02_core_commands.sql`
