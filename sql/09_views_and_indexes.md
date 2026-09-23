# SQL Tutorial 9: Views and Indexes

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 9 - Views & Indexes](https://analyticsmadesimple.com/tutorials/sql-tutorial-9-views-and-indexes/)**
> Raw Script: [`09_views_and_indexes.sql`](./09_views_and_indexes.sql)

Views create simplified, reusable virtual tables, while B-tree indexes drastically accelerate search performance on high-volume tables.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`09_views_and_indexes.sql`](./09_views_and_indexes.sql):

```sql
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
```

---

## Performance Impact

1. **Reporting Views:** Instead of repeatedly writing a 10-line `JOIN` and `GROUP BY` query across dashboards, business analysts can simply run:
   ```sql
   SELECT * FROM v_customer_order_summary WHERE region = 'Europe';
   ```
2. **Composite Indexes:** `CREATE INDEX idx_orders_status_date ON orders(status, order_date)` allows the database engine to perform a rapid binary search directly to `completed` orders in February without scanning every single row in the table.

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/09_views_and_indexes.sql
```

👉 Next: [Part 10: Advanced SQL Techniques](./10_advanced_ctes_window_functions.md)
