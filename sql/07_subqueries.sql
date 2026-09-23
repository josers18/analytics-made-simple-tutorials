-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 7: Subqueries in SQL (https://analyticsmadesimple.com/tutorials/sql-tutorial-7-subqueries/)
-- License: MIT

-- 1. Scalar Subquery: Orders greater than the overall average order value
SELECT 
    order_id, 
    customer_id, 
    order_total
FROM orders
WHERE order_total > (SELECT AVG(order_total) FROM orders);

-- 2. Subquery with IN: Customers who placed orders in March 2025
SELECT customer_id, name, region
FROM customers
WHERE customer_id IN (
    SELECT DISTINCT customer_id 
    FROM orders 
    WHERE order_date >= '2025-03-01'
);

-- 3. Correlated Subquery with EXISTS: Customers with at least one completed order
SELECT c.customer_id, c.name
FROM customers c
WHERE EXISTS (
    SELECT 1 
    FROM orders o 
    WHERE o.customer_id = c.customer_id 
      AND o.status = 'completed'
);
