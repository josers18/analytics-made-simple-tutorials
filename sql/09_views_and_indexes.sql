-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 9: Views and Indexes (https://analyticsmadesimple.com/tutorials/sql-tutorial-9-views-and-indexes/)
-- License: MIT

-- 1. Create a View for Reporting
CREATE VIEW IF NOT EXISTS v_customer_order_summary AS
SELECT 
    c.customer_id,
    c.name,
    c.region,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.order_total), 0) AS total_revenue
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'completed'
GROUP BY c.customer_id, c.name, c.region;

-- Query the View like a standard table
SELECT * FROM v_customer_order_summary WHERE total_revenue > 1000;

-- 2. Create B-Tree Indexes for Fast Lookups
CREATE INDEX IF NOT EXISTS idx_orders_customer_id ON orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_orders_status_date ON orders(status, order_date);
CREATE INDEX IF NOT EXISTS idx_order_lines_order_id ON order_lines(order_id);

-- 3. Verify Index Utilization with EXPLAIN QUERY PLAN
EXPLAIN QUERY PLAN
SELECT * FROM orders
WHERE status = 'completed' AND order_date >= '2025-02-01';
