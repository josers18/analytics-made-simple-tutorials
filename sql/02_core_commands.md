# SQL Tutorial 2: Master the Core Commands

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 2 - Core Commands](https://analyticsmadesimple.com/tutorials/sql-tutorial-2-core-commands/)**
> Raw Script: [`02_core_commands.sql`](./02_core_commands.sql)

The four fundamental verbs of SQL are **SELECT**, **INSERT**, **UPDATE**, and **DELETE** (often referred to as CRUD: Create, Read, Update, Delete).

---

## The Complete SQL Script

Below is the complete SQL script contained in [`02_core_commands.sql`](./02_core_commands.sql):

```sql
-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 2: Master the Core Commands (https://analyticsmadesimple.com/tutorials/sql-tutorial-2-core-commands/)
-- License: MIT

-- SELECT: Inspect customer data
SELECT customer_id, name, region FROM customers;

-- INSERT: Add a new client
INSERT INTO customers (customer_id, name, email, region, created_at)
VALUES (6, 'Horizon Media', 'contact@horizonmedia.com', 'North America', '2025-03-20 14:00:00');

-- UPDATE: Modify customer attributes safely with WHERE
UPDATE customers
SET region = 'Latin America'
WHERE customer_id = 6;

-- DELETE: Remove records with explicit filters
DELETE FROM customers
WHERE customer_id = 6;

-- Verification
SELECT * FROM customers ORDER BY customer_id;
```

---

## Step-by-Step Breakdown

### 1. `SELECT`: Reading Data
```sql
SELECT customer_id, name, region FROM customers;
```
* **Best Practice:** Always specify explicit column names rather than `SELECT *`. In production environments, explicit column projection reduces network transfer overhead and protects applications from breaking when upstream table schemas change.

### 2. `INSERT`: Adding Records
```sql
INSERT INTO customers (customer_id, name, email, region, created_at)
VALUES (6, 'Horizon Media', 'contact@horizonmedia.com', 'North America', '2025-03-20 14:00:00');
```
* Explicitly listing column names in parentheses before `VALUES` ensures your query will not fail if new columns are added to the table later.

### 3. `UPDATE`: Changing Existing Rows
```sql
UPDATE customers
SET region = 'Latin America'
WHERE customer_id = 6;
```
* **Golden Rule:** **Always test your `WHERE` clause with a `SELECT` first.** Running `UPDATE customers SET region = 'Latin America';` without a `WHERE` clause will overwrite every single customer row in your database!

### 4. `DELETE`: Removing Rows
```sql
DELETE FROM customers
WHERE customer_id = 6;
```
* Similar to `UPDATE`, executing `DELETE` without a `WHERE` clause wipes the entire table.

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/02_core_commands.sql
```

👉 Next: [Part 3: Retrieving Data with SELECT](./03_select_queries.md)
