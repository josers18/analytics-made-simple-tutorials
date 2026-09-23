-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 3: Retrieving Data with SELECT (https://analyticsmadesimple.com/tutorials/sql-tutorial-3-select/)
-- License: MIT

-- 1. Explicit Column Selection with Aliases
SELECT 
    name AS customer_name,
    email AS contact_email,
    region AS sales_territory
FROM customers;

-- 2. Computed Columns & Mathematical Expressions
SELECT 
    order_id,
    order_total,
    order_total * 0.0825 AS estimated_tax,
    order_total * 1.0825 AS gross_total_with_tax
FROM orders;

-- 3. Distinct Unique Values
SELECT DISTINCT region FROM customers;
SELECT DISTINCT status FROM orders;
