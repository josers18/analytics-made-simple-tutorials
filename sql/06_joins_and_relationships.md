# SQL Tutorial 6: Joins in SQL

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 6 - Joins in SQL](https://analyticsmadesimple.com/tutorials/sql-tutorial-6-joins-in-sql/)**
> Raw Script: [`06_joins_and_relationships.sql`](./06_joins_and_relationships.sql)

In a normalized relational database, related information is distributed across multiple tables. Joins allow you to stitch them back together on shared keys.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`06_joins_and_relationships.sql`](./06_joins_and_relationships.sql):

```sql
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
    ol.product_name,
    ol.quantity,
    ol.unit_price,
    (ol.quantity * ol.unit_price) AS line_total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_lines ol ON o.order_id = ol.order_id
ORDER BY o.order_id, ol.line_id;
```

---

## Join Mechanics

```text
INNER JOIN: Only returns rows where keys exist in BOTH tables.
[Customers] ∩ [Orders]

LEFT JOIN: Returns ALL rows from the left table, plus matching rows from the right table.
[Customers]  <---  [Matching Orders or NULL]
```

### Notice the Difference:
In Query 2 (`LEFT JOIN`), customer #5 (`Delta Dynamics`) appears in the results with `NULL` for `order_id` and `order_total` because they have never placed an order. An `INNER JOIN` would drop Delta Dynamics entirely!

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/06_joins_and_relationships.sql
```

👉 Next: [Part 7: Subqueries in SQL](./07_subqueries.md)
