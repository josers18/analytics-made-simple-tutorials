# SQL Tutorial 10: Advanced SQL Techniques

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 10 - Advanced SQL](https://analyticsmadesimple.com/tutorials/sql-tutorial-10-advanced-sql-techniques/)**
> Raw Script: [`10_advanced_ctes_window_functions.sql`](./10_advanced_ctes_window_functions.sql)

Common Table Expressions (`WITH`) make complex multi-step queries readable, while Window Functions (`OVER`) allow you to calculate rankings and running totals without collapsing rows.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`10_advanced_ctes_window_functions.sql`](./10_advanced_ctes_window_functions.sql):

```sql
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
```

---

## Key Output Walkthrough

### 1. Percentage of Total via CTE
```text
region          regional_revenue  pct_of_total
--------------  ----------------  ------------
Europe          3100.0            42.18
North America   2270.0            30.88
Asia-Pacific    1980.0            26.94
```

### 2. Window Running Revenue
Unlike `GROUP BY`, which reduces multiple rows into one, the window function `SUM(order_total) OVER (...)` retains every individual order while computing cumulative revenue as of each date:

| order_id | order_date | order_total | running_revenue |
|:---|:---|:---|:---|
| 101 | 2025-02-10 | $1,450.00 | $1,450.00 |
| 102 | 2025-02-25 | $820.00 | $2,270.00 |
| 103 | 2025-03-01 | $3,100.00 | $5,370.00 |
| 105 | 2025-03-12 | $1,980.00 | $7,350.00 |

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/10_advanced_ctes_window_functions.sql
```

👉 Next: [Part 11: Stored Procedures & Triggers](./11_stored_procedures_triggers.md)
