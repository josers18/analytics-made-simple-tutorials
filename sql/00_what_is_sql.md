# SQL Tutorial 0: What is SQL and Why Learn It?

> **Official Companion Guide for [Analytics Made Simple: What is SQL?](https://analyticsmadesimple.com/tutorials/what-is-sql/)**

SQL (Structured Query Language) is the universal standard for asking precise questions of structured data. While spreadsheets give you a visual canvas for small ad-hoc tables, relational databases and SQL provide the engine for high-volume, reliable data systems.

---

## Core Concepts

### 1. The Relational Model
Data is organized into **tables** (relations) consisting of **rows** (records) and **columns** (attributes).
* **Primary Key (PK):** A unique identifier for each row (e.g., `customer_id`).
* **Foreign Key (FK):** A column that references the primary key of another table (e.g., `orders.customer_id` referencing `customers.customer_id`).

### 2. SQL vs. Spreadsheets

| Dimension | Spreadsheets (Excel / Sheets) | Relational SQL Databases (PostgreSQL / SQLite) |
|---|---|---|
| **Data Capacity** | ~1M rows maximum; slows down >100k rows | Millions to billions of rows with indexing |
| **Integrity & Constraints** | Accidental cell overwrites, loose data types | Strict schema enforcement, types, foreign key integrity |
| **Concurrent Users** | Version conflicts, locked files | Thousands of simultaneous reads and transactions (ACID) |
| **Reproducibility** | Manual copy-paste, hidden formula edits | Scriptable, version-controlled queries with exact lineage |

### 3. Popular SQL Engines
* **SQLite:** Embedded, zero-configuration, single-file database. Perfect for practice, mobile apps, and edge analytics.
* **PostgreSQL:** The gold-standard open-source production database. Supports rich data types, JSON, window functions, and extensions.
* **DuckDB:** The "SQLite for analytics" — columnar, vectorized execution engine designed for local analytical processing and Parquet queries.

---

## Next Steps
Proceed to [Part 1: Setting Up Your SQL Playground](./01_playground_setup.md) to initialize your local practice database.
