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
