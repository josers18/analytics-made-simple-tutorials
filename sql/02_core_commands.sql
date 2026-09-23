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
