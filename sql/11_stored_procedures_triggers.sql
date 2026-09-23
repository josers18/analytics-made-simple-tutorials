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
