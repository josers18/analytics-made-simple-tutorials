# SQL Tutorial 3: Retrieving Data with SELECT

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 3 - SELECT](https://analyticsmadesimple.com/tutorials/sql-tutorial-3-select/)**
> Raw Script: [`03_select_queries.sql`](./03_select_queries.sql)

The `SELECT` statement is the cornerstone of data analytics. This tutorial covers column aliasing (`AS`), calculated expressions, and removing duplicates with `DISTINCT`.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`03_select_queries.sql`](./03_select_queries.sql):

```sql
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
```

---

## Query Breakdown & Expected Output

### Query 1: Column Aliasing
Aliasing with `AS` renames output columns for reporting clarity:
```sql
SELECT 
    name AS customer_name,
    email AS contact_email,
    region AS sales_territory
FROM customers;
```

| customer_name | contact_email | sales_territory |
|:---|:---|:---|
| Acme Industrial | ops@acmeind.com | North America |
| Apex Logistics | dispatch@apexlog.com | Europe |
| Beacon Health | admin@beaconhlth.org | North America |
| Crestview Retail | orders@crestview.com | Asia-Pacific |
| Delta Dynamics | billing@deltadyn.io | Europe |

### Query 2: Mathematical Calculations
SQL functions as an on-the-fly calculation engine for business logic:
```sql
SELECT 
    order_id,
    order_total,
    order_total * 0.0825 AS estimated_tax,
    order_total * 1.0825 AS gross_total_with_tax
FROM orders;
```

| order_id | order_total | estimated_tax | gross_total_with_tax |
|:---|:---|:---|:---|
| 101 | 1450.00 | 119.625 | 1569.625 |
| 102 | 820.00 | 67.650 | 887.650 |
| 103 | 3100.00 | 255.750 | 3355.750 |

### Query 3: Finding Unique Values with `DISTINCT`
```sql
SELECT DISTINCT region FROM customers;
```

| region |
|:---|
| North America |
| Europe |
| Asia-Pacific |

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/03_select_queries.sql
```

👉 Next: [Part 4: Filtering and Sorting Data in SQL](./04_filtering_and_sorting.md)
