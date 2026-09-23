-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 6: Joins in SQL (https://analyticsmadesimple.com/tutorials/sql-tutorial-6-joins-in-sql/)
-- License: MIT

-- 1. INNER JOIN: Customers with their orders (drops customers with 0 orders)
SELECT 
    c.customer_id,
    c.name,
    o.order_id,
    o.order_date,
    o.order_total
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;

-- 2. LEFT JOIN: All customers, including those who have never placed an order
SELECT 
    c.customer_id,
    c.name,
    c.region,
    o.order_id,
    o.order_total
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_id;

-- 3. Multi-table Join: Customer -> Order -> Line Items
SELECT 
    c.name AS customer_name,
    o.order_id,
    l.product_name,
    l.quantity,
    l.unit_price,
    (l.quantity * l.unit_price) AS line_subtotal
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_lines l ON o.order_id = l.order_id
ORDER BY o.order_id, l.line_id;

-- 4. Preventing Fan-Out Aggregation Trap
-- Warning: Joining orders to line items multiplies order rows. 
-- Aggregate line items first before joining to orders.
WITH line_totals AS (
    SELECT 
        order_id,
        SUM(quantity * unit_price) AS calculated_lines_total
    FROM order_lines
    GROUP BY order_id
)
SELECT 
    o.order_id,
    o.order_total AS header_total,
    COALESCE(lt.calculated_lines_total, 0) AS lines_total
FROM orders o
LEFT JOIN line_totals lt ON o.order_id = lt.order_id;
