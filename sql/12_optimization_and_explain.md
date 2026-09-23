# SQL Tutorial 12: Best Practices & Optimization

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 12 - Optimization](https://analyticsmadesimple.com/tutorials/sql-tutorial-12-best-practices-and-optimization/)**
> Raw Script: [`12_optimization_and_explain.sql`](./12_optimization_and_explain.sql)

Writing queries that execute in milliseconds instead of minutes requires understanding **sargability** (Search Argument Able) and analyzing query plans with `EXPLAIN`.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`12_optimization_and_explain.sql`](./12_optimization_and_explain.sql):

```sql
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
```

---

## The Sargability Trap

When an index exists on `order_date`, wrapping that column in a function like `strftime('%Y', order_date)` prevents the database engine from using the index, forcing a costly **Full Table Scan (SCAN TABLE)**.

By rewriting the condition as an explicit range comparison (`WHERE order_date >= '2025-01-01' AND order_date < '2026-01-01'`), the query becomes **sargable**, allowing the query planner to execute a rapid **Index Search (SEARCH TABLE)**.

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/12_optimization_and_explain.sql
```

👉 Next: [Part 13: Maintenance & Growth Strategies](./13_database_maintenance.md)
