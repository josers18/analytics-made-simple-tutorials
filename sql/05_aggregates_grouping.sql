-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 5: Aggregate Functions and Grouping Data (https://analyticsmadesimple.com/tutorials/sql-tutorial-5-aggr-grouping/)
-- License: MIT

-- 1. Table-wide Summary Statistics
SELECT 
    COUNT(*) AS total_orders,
    SUM(order_total) AS gross_revenue,
    AVG(order_total) AS average_order_value,
    MIN(order_total) AS smallest_order,
    MAX(order_total) AS largest_order
FROM orders;

-- 2. Grouping by Dimension
SELECT 
    customer_id,
    COUNT(order_id) AS order_count,
    SUM(order_total) AS customer_spend
FROM orders
GROUP BY customer_id
ORDER BY customer_spend DESC;

-- 3. Filtering Grouped Results with HAVING
-- Note: WHERE filters rows before aggregation; HAVING filters groups after aggregation.
SELECT 
    customer_id,
    COUNT(order_id) AS completed_orders,
    SUM(order_total) AS total_spend
FROM orders
WHERE status = 'completed'
GROUP BY customer_id
HAVING SUM(order_total) >= 1000.00;
