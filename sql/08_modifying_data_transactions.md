# SQL Tutorial 8: Modifying Data & Transactions

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 8 - Modifying Data](https://analyticsmadesimple.com/tutorials/sql-tutorial-8-modifying-data-with-sql/)**
> Raw Script: [`08_modifying_data_transactions.sql`](./08_modifying_data_transactions.sql)

Transactions group multiple database operations into a single atomic unit. Either all operations succeed (`COMMIT`), or all are safely reverted (`ROLLBACK`).

---

## The Complete SQL Script

Below is the complete SQL script contained in [`08_modifying_data_transactions.sql`](./08_modifying_data_transactions.sql):

```sql
-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 8: Modifying Data with SQL (https://analyticsmadesimple.com/tutorials/sql-tutorial-8-modifying-data-with-sql/)
-- License: MIT

-- 1. Atomic Transaction with ROLLBACK demonstration
BEGIN TRANSACTION;

-- Place a test update
UPDATE orders
SET order_total = order_total * 1.10
WHERE status = 'pending';

-- Verify changes inside transaction
SELECT * FROM orders WHERE status = 'pending';

-- Discard changes safely
ROLLBACK;

-- 2. Committed Transaction: Creating an Order and Line Items atomically
BEGIN TRANSACTION;

INSERT INTO orders (order_id, customer_id, order_date, status, order_total)
VALUES (107, 3, '2025-03-22', 'completed', 750.00);

INSERT INTO order_lines (line_id, order_id, product_name, quantity, unit_price)
VALUES (9, 107, 'Industrial Gateway', 1, 750.00);

COMMIT;

-- Verify insertion
SELECT * FROM orders WHERE order_id = 107;
```

---

## The ACID Principles

| Principle | Meaning | Production Real-World Benefit |
|:---|:---|:---|
| **Atomicity** | All or nothing | An order and its line items are created together or not at all. |
| **Consistency** | Invariants hold | Database constraints (`CHECK`, `FOREIGN KEY`) are enforced. |
| **Isolation** | Independent concurrency | Concurrent queries cannot see intermediate uncommitted states. |
| **Durability** | Persisted to disk | Once committed, data survives power outages and crashes. |

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/08_modifying_data_transactions.sql
```

👉 Next: [Part 9: Views and Indexes](./09_views_and_indexes.md)
