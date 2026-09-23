# Python Tutorial 3: Selecting, Filtering, and Sorting in Pandas

> **Official Companion Guide for [Analytics Made Simple: Selecting, Filtering, and Sorting in Pandas](https://analyticsmadesimple.com/tutorials/)**
> Raw Script: [`03_selecting_filtering_sorting.py`](./03_selecting_filtering_sorting.py)

Translate SQL `WHERE`, `IN`, and `ORDER BY` clauses directly into vector-accelerated pandas operations.

---

## The Complete Python Script

Below is the complete script contained in [`03_selecting_filtering_sorting.py`](./03_selecting_filtering_sorting.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Selecting, Filtering, and Sorting in Pandas
License: MIT
"""

import pandas as pd

# Load sample dataset
df = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106],
    "customer": ["Acme Industrial", "Acme Industrial", "Apex Logistics", "Beacon Health", "Crestview Retail", "Apex Logistics"],
    "region": ["North America", "North America", "Europe", "North America", "Asia-Pacific", "Europe"],
    "order_total": [1450.00, 820.00, 3100.00, 450.00, 1980.00, 650.00],
    "status": ["completed", "completed", "completed", "pending", "completed", "cancelled"]
})

# 1. Column Selection (SELECT order_id, customer, order_total)
selected = df[["order_id", "customer", "order_total"]]
print("=== Selected Columns ===")
print(selected)

# 2. Boolean Filtering (WHERE status = 'completed' AND order_total >= 1000)
high_value_completed = df[(df["status"] == "completed") & (df["order_total"] >= 1000.00)]
print("\n=== High Value Completed Orders ===")
print(high_value_completed)

# 3. Range Filtering (WHERE region IN ('Europe', 'Asia-Pacific'))
international = df[df["region"].isin(["Europe", "Asia-Pacific"])]
print("\n=== International Orders ===")
print(international)

# 4. Sorting (ORDER BY region ASC, order_total DESC)
sorted_df = df.sort_values(by=["region", "order_total"], ascending=[True, False])
print("\n=== Sorted DataFrame ===")
print(sorted_df)
```

---

## SQL to Pandas Rosetta Stone

| SQL Syntax | Pandas Vectorized Expression |
|:---|:---|
| `SELECT col1, col2` | `df[["col1", "col2"]]` |
| `WHERE status = 'active'` | `df[df["status"] == "active"]` |
| `WHERE colA = 1 AND colB > 5` | `df[(df["colA"] == 1) & (df["colB"] > 5)]` *(Note: use `&` and wrap conditions in parentheses)* |
| `WHERE region IN ('A', 'B')` | `df[df["region"].isin(["A", "B"])]` |
| `ORDER BY region ASC, total DESC` | `df.sort_values(by=["region", "total"], ascending=[True, False])` |

---

## How to Run

```bash
python3 python/03_selecting_filtering_sorting.py
```

👉 Next: [Part 4: Standardizing Categories and Names](./04_standardizing_categories_and_names.md)
