-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 12: Best Practices and Optimization (https://analyticsmadesimple.com/tutorials/sql-tutorial-12-best-practices-and-optimization/)
-- License: MIT

-- 1. Non-Sargable Query Anti-Pattern (Forces Full Table Scan)
-- Using a function on an indexed column prevents index usage:
-- EXPLAIN QUERY PLAN SELECT * FROM orders WHERE strftime('%Y', order_date) = '2025';

-- 2. Sargable Equivalent (Utilizes Index Range Scan)
EXPLAIN QUERY PLAN
SELECT * FROM orders
WHERE order_date >= '2025-01-01' AND order_date < '2026-01-01';

-- 3. Avoid SELECT * in Analytical Aggregations
SELECT 
    customer_id, 
    COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id;
