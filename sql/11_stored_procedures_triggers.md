# SQL Tutorial 11: Stored Procedures & Triggers

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 11 - Stored Procedures & Triggers](https://analyticsmadesimple.com/tutorials/sql-tutorial-11-stored-procedures-triggers-and-user-defined-functions/)**
> Raw Script: [`11_stored_procedures_triggers.sql`](./11_stored_procedures_triggers.sql)

Event triggers automate database auditing, validation, and change logging right at the database layer.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`11_stored_procedures_triggers.sql`](./11_stored_procedures_triggers.sql):

```sql
-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 11: Stored Procedures, Triggers, and User-Defined Functions
-- https://analyticsmadesimple.com/tutorials/sql-tutorial-11-stored-procedures-triggers-and-user-defined-functions/
-- License: MIT

-- 1. Create Audit Table
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INTEGER PRIMARY KEY,
    table_name TEXT NOT NULL,
    action TEXT NOT NULL,
    record_id INTEGER NOT NULL,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Create Trigger on Order Creation (SQLite compatible)
CREATE TRIGGER IF NOT EXISTS trg_after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, action, record_id)
    VALUES ('orders', 'INSERT', NEW.order_id);
END;

-- Test the Trigger
INSERT INTO orders (order_id, customer_id, order_date, status, order_total)
VALUES (108, 1, '2025-03-25', 'pending', 350.00);

-- Verify Audit Trail
SELECT * FROM audit_log ORDER BY log_id DESC;
```

---

## Audit Verification Output

When order `#108` is inserted into `orders`, SQLite automatically fires `trg_after_order_insert`, writing to `audit_log`:

| log_id | table_name | action | record_id | changed_at |
|:---|:---|:---|:---|:---|
| 1 | orders | INSERT | 108 | 2025-03-25 15:00:00 |

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/11_stored_procedures_triggers.sql
```

👉 Next: [Part 12: Best Practices & Optimization](./12_optimization_and_explain.md)
