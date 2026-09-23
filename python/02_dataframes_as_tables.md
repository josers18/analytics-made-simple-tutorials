# Python Tutorial 2: DataFrames as Tables

> **Official Companion Guide for [Analytics Made Simple: DataFrames as Tables](https://analyticsmadesimple.com/tutorials/)**
> Raw Script: [`02_dataframes_as_tables.py`](./02_dataframes_as_tables.py)

Understand pandas `DataFrame` structures through the lens of relational SQL tables, column schemas, and summary statistics.

---

## The Complete Python Script

Below is the complete script contained in [`02_dataframes_as_tables.py`](./02_dataframes_as_tables.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: DataFrames as Tables
License: MIT
"""

import pandas as pd
import numpy as np

# 1. Creating a DataFrame from raw records (analogous to a SQL table)
data = {
    "order_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 1, 2, 3, 4],
    "region": ["North America", "North America", "Europe", "North America", "Asia-Pacific"],
    "order_total": [1450.00, 820.00, 3100.00, 450.00, 1980.00],
    "status": ["completed", "completed", "completed", "pending", "completed"]
}

df = pd.DataFrame(data)

# 2. Inspecting Shape and Schema (like PRAGMA table_info or DESCRIBE)
print("=== DataFrame Schema & Types ===")
print(df.info())

print("\n=== Summary Statistics (like SQL AVG/MIN/MAX) ===")
print(df.describe())

# 3. Viewing Top Rows (like SELECT * FROM orders LIMIT 3)
print("\n=== Head (Limit 3) ===")
print(df.head(3))
```

---

## Concepts & Output Walkthrough

1. **`df.info()` vs `DESCRIBE table`:** Prints column names, non-null counts, and inferred data types (`int64`, `object`, `float64`).
2. **`df.describe()` vs SQL Aggregations:** Computes count, mean, std, min, 25%, 50% (median), 75%, and max across numeric columns in a single vectorized pass.
3. **`df.head(3)` vs `LIMIT 3`:** Returns the first 3 rows of the table:

```text
   order_id  customer_id         region  order_total     status
0       101            1  North America       1450.0  completed
1       102            1  North America        820.0  completed
2       103            2         Europe       3100.0  completed
```

---

## How to Run

```bash
python3 python/02_dataframes_as_tables.py
```

👉 Next: [Part 3: Selecting, Filtering, and Sorting in Pandas](./03_selecting_filtering_sorting.md)
