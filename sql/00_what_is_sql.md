# SQL Tutorial 0: What is SQL and Why Learn It?

> **Official Companion Guide for [Analytics Made Simple: What is SQL?](https://analyticsmadesimple.com/tutorials/what-is-sql/)**

SQL (Structured Query Language) is the universal standard for querying, transforming, and managing structured data. While spreadsheets give you a visual canvas for small ad-hoc tables, relational databases and SQL provide the engine for high-volume, reliable data systems.

---

## Core Concepts

### 1. The Relational Model
Data is organized into **tables** (relations) consisting of **rows** (records) and **columns** (attributes).
* **Primary Key (PK):** A unique identifier for each row (e.g., `customer_id`).
* **Foreign Key (FK):** A column that references the primary key of another table (e.g., `orders.customer_id` referencing `customers.customer_id`).

### 2. SQL vs. Spreadsheets

| Dimension | Spreadsheets (Excel / Sheets) | Relational SQL Databases (PostgreSQL / SQLite) |
|:---|:---|:---|
| **Max Scale** | ~1 million rows (slows down at 100k) | Billions of rows with B-Tree indexes |
| **Data Integrity** | Prone to copy-paste drift, mixed types | Enforced schemas, types, and constraints |
| **Concurrency** | Lockups on multi-user writes | ACID transactions and row-level locking |
| **Automation** | Fragile macros and manual exports | Programmatic scheduled queries and pipelines |

---

## The Core SQL Grammar in Action

Here is what foundational SQL looks like. You can run these commands directly in any standard database engine:

```sql
-- 1. Create a table with defined types and constraints
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    region TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Insert structured records
INSERT INTO customers (customer_id, name, region) VALUES
(1, 'Acme Industrial', 'North America'),
(2, 'Apex Logistics', 'Europe'),
(3, 'Beacon Health', 'North America');

-- 3. Query the data with filtering and column selection
SELECT 
    customer_id, 
    name, 
    region 
FROM customers 
WHERE region = 'North America'
ORDER BY customer_id;
```

### Expected Query Output

| customer_id | name | region |
|:---|:---|:---|
| 1 | Acme Industrial | North America |
| 3 | Beacon Health | North America |

---

## Next Steps

Now that you understand what SQL is and why it powers every modern analytics stack, set up your safe local database environment:

👉 Next: [Part 1: Setting Up Your SQL Playground](./01_playground_setup.md)
