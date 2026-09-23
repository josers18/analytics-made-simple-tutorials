-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 4: Filtering and Sorting Data in SQL (https://analyticsmadesimple.com/tutorials/sql-tutorial-4-filter-sort/)
-- License: MIT

-- 1. Exact Filtering
SELECT * FROM orders WHERE status = 'completed';

-- 2. Multiple Conditions with AND / OR
SELECT * FROM orders
WHERE status = 'completed' AND order_total >= 1000.00;

-- 3. Range Filtering with BETWEEN
SELECT * FROM orders
WHERE order_date BETWEEN '2025-02-01' AND '2025-02-28';

-- 4. Set Membership with IN
SELECT * FROM customers
WHERE region IN ('North America', 'Europe');

-- 5. Wildcard Matching with LIKE
SELECT * FROM customers WHERE email LIKE '%.org';
SELECT * FROM customers WHERE name LIKE 'A%';

-- 6. Sorting with ORDER BY (Multi-column)
SELECT order_id, customer_id, order_date, order_total
FROM orders
ORDER BY order_date DESC, order_total ASC;

-- 7. Pagination with LIMIT and OFFSET
SELECT * FROM orders
ORDER BY order_date DESC
LIMIT 3 OFFSET 0;
