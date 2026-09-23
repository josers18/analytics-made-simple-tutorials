# SQL Tutorial 7: Subqueries in SQL

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 7 - Subqueries](https://analyticsmadesimple.com/tutorials/sql-tutorial-7-subqueries/)**
> Raw Script: [`07_subqueries.sql`](./07_subqueries.sql)

Subqueries are queries nested inside another SQL statement. They let you perform dynamic calculations or filtering without multi-step manual procedures.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`07_subqueries.sql`](./07_subqueries.sql):

```sql
-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 7: Subqueries in SQL (https://analyticsmadesimple.com/tutorials/sql-tutorial-7-subqueries/)
-- License: MIT

-- 1. Scalar Subquery in WHERE: Orders above the average order value
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
```

---

## Subquery Patterns Explained

1. **Scalar Subqueries:** Returns a single value (1 row, 1 column). In Query 1, `(SELECT AVG(order_total) FROM orders)` evaluates to `1408.33`, and then filters orders above that average.
2. **List Subqueries with `IN`:** Returns a single column with multiple rows. Evaluated once before the outer query runs.
3. **Correlated Subqueries with `EXISTS`:** References columns from the outer query (`c.customer_id`). The database checks each customer row and halts evaluation as soon as a single matching record is found (`SELECT 1`).

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/07_subqueries.sql
```

👉 Next: [Part 8: Modifying Data & Transactions](./08_modifying_data_transactions.md)
