# SQL Tutorial 5: Aggregate Functions and Grouping Data

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 5 - Aggregates & Grouping](https://analyticsmadesimple.com/tutorials/sql-tutorial-5-aggr-grouping/)**
> Raw Script: [`05_aggregates_grouping.sql`](./05_aggregates_grouping.sql)

Aggregations collapse thousands of raw operational records into high-level business metrics like revenue, order counts, and averages.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`05_aggregates_grouping.sql`](./05_aggregates_grouping.sql):

```sql
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
```

---

## Critical Distinction: `WHERE` vs `HAVING`

* **`WHERE` executes BEFORE aggregation.** It filters individual underlying rows before any math occurs (e.g. `WHERE status = 'completed'`).
* **`HAVING` executes AFTER aggregation.** It filters the summarized groups based on calculated metrics (e.g. `HAVING SUM(order_total) >= 1000.00`).

### Expected Output for Query 3

| customer_id | completed_orders | total_spend |
|:---|:---|:---|
| 2 | 1 | $3,100.00 |
| 1 | 2 | $2,270.00 |
| 4 | 1 | $1,980.00 |

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/05_aggregates_grouping.sql
```

👉 Next: [Part 6: Joins in SQL](./06_joins_and_relationships.md)
