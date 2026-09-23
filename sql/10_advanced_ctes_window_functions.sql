-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 10: Advanced SQL Techniques (https://analyticsmadesimple.com/tutorials/sql-tutorial-10-advanced-sql-techniques/)
-- License: MIT

-- 1. Common Table Expression (CTE)
WITH regional_performance AS (
    SELECT 
        c.region,
        COUNT(o.order_id) AS order_volume,
        SUM(o.order_total) AS regional_revenue
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    WHERE o.status = 'completed'
    GROUP BY c.region
)
SELECT 
    region,
    regional_revenue,
    ROUND(regional_revenue * 100.0 / (SELECT SUM(regional_revenue) FROM regional_performance), 2) AS pct_of_total
FROM regional_performance
ORDER BY regional_revenue DESC;

-- 2. Window Functions: Ranking within Partitions
SELECT 
    o.order_id,
    c.region,
    c.name,
    o.order_total,
    ROW_NUMBER() OVER (PARTITION BY c.region ORDER BY o.order_total DESC) AS rank_in_region
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.status = 'completed';

-- 3. Window Functions: Running Totals
SELECT 
    order_id,
    order_date,
    order_total,
    SUM(order_total) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_revenue
FROM orders
WHERE status = 'completed';
