# SQL Tutorial 4: Filtering and Sorting Data in SQL

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 4 - Filter & Sort](https://analyticsmadesimple.com/tutorials/sql-tutorial-4-filter-sort/)**
> Raw Script: [`04_filtering_and_sorting.sql`](./04_filtering_and_sorting.sql)

Filtering (`WHERE`) and sorting (`ORDER BY`) allow you to isolate the precise slice of data required for any analytical question.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`04_filtering_and_sorting.sql`](./04_filtering_and_sorting.sql):

```sql
-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 4: Filtering and Sorting Data in SQL (https://analyticsmadesimple.com/tutorials/sql-tutorial-4-filter-sort/)
-- License: MIT

-- 1. Exact Filtering
SELECT * FROM orders WHERE status = 'completed';

-- 2. Multiple Conditions with AND / OR
SELECT * FROM orders
WHERE status = 'completed' AND order_total >= 1000.00;

-- 3. Range Filtering with BETWEEN
SELECT * FROM orders
WHERE order_date BETWEEN '2025-02-01' AND '2025-02-28';

-- 4. Set Membership with IN
SELECT * FROM customers
WHERE region IN ('North America', 'Europe');

-- 5. Wildcard Matching with LIKE
SELECT * FROM customers WHERE email LIKE '%.org';
SELECT * FROM customers WHERE name LIKE 'A%';

-- 6. Sorting with ORDER BY (Multi-column)
SELECT order_id, customer_id, order_date, order_total
FROM orders
ORDER BY order_date DESC, order_total ASC;

-- 7. Pagination with LIMIT and OFFSET
SELECT * FROM orders
ORDER BY order_date DESC
LIMIT 3 OFFSET 0;
```

---

## Key Operators Explained

| Operator | Usage | Purpose |
|:---|:---|:---|
| `=` / `!=` | `status = 'completed'` | Exact equality / inequality match |
| `AND` / `OR` | `status = 'completed' AND total > 1000` | Combining logical conditions |
| `BETWEEN` | `date BETWEEN '2025-01-01' AND '2025-01-31'` | Inclusive numeric or date range check |
| `IN` | `region IN ('Europe', 'Asia-Pacific')` | Compact set membership check |
| `LIKE` | `email LIKE '%.org'` | Pattern matching (`%` matches any characters, `_` matches single char) |
| `ORDER BY` | `ORDER BY date DESC, total ASC` | Primary and secondary result ordering |
| `LIMIT / OFFSET`| `LIMIT 10 OFFSET 20` | Database-level pagination (Page 3 with 10 per page) |

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/04_filtering_and_sorting.sql
```

👉 Next: [Part 5: Aggregate Functions and Grouping Data](./05_aggregates_grouping.md)
