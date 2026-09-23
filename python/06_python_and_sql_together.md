# Python Tutorial 6: Python and SQL Together

> **Official Companion Guide for [Analytics Made Simple: Python and SQL Together](https://analyticsmadesimple.com/tutorials/)**
> Raw Script: [`06_python_and_sql_together.py`](./06_python_and_sql_together.py)

Learn the bi-directional bridge between relational SQL databases and pandas analytics pipelines.

---

## The Complete Python Script

Below is the complete script contained in [`06_python_and_sql_together.py`](./06_python_and_sql_together.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Python and SQL Together
License: MIT
"""

import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect(":memory:")

# Seed database with sample orders
conn.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_total DECIMAL(10, 2),
    status TEXT
)
""")
conn.executemany(
    "INSERT INTO orders VALUES (?, ?, ?, ?)",
    [
        (101, 1, 1450.00, "completed"),
        (102, 1, 820.00, "completed"),
        (103, 2, 3100.00, "completed"),
        (104, 3, 450.00, "pending"),
        (105, 4, 1980.00, "completed")
    ]
)
conn.commit()

# 1. Query directly into pandas DataFrame
query = "SELECT customer_id, SUM(order_total) AS total_spend FROM orders WHERE status = 'completed' GROUP BY customer_id"
df_summary = pd.read_sql_query(query, conn)
print("=== SQL Aggregation Loaded into Pandas ===")
print(df_summary)

# 2. Enrich in Python with business categorization
def segment_customer(spend):
    if spend >= 2500:
        return "Tier 1 Enterprise"
    elif spend >= 1000:
        return "Tier 2 Mid-Market"
    return "Tier 3 SMB"

df_summary["customer_tier"] = df_summary["total_spend"].apply(segment_customer)

# 3. Write enriched data back to SQL
df_summary.to_sql("customer_segments", conn, index=False, if_exists="replace")

# Verify written table in SQL
res = pd.read_sql_query("SELECT * FROM customer_segments", conn)
print("\n=== Enriched Table Read Back from SQL ===")
print(res)
```

---

## Pipeline Architecture

```text
[Relational Database] 
       │  (Heavy filtering & aggregations via SQL)
       ▼
  pd.read_sql_query()
       ▼
 [Pandas DataFrame]
       │  (Complex business logic, ML inference, NLP)
       ▼
      df.to_sql()
       ▼
[Persistent Analytical Table]
```

---

## How to Run

```bash
python3 python/06_python_and_sql_together.py
```

🎓 Explore the next track: [TypeSafe AI & Decision Engines](../typesafe-ai/README.md)
