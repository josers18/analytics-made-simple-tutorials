# Python Tutorial 5: Grain Verification and Hand-Off

> **Official Companion Guide for [Analytics Made Simple: Pandas Export and Hand-Off](https://analyticsmadesimple.com/analytics/pandas-export-and-hand-off/)**
> Raw Script: [`05_verify_grain_and_export.py`](./05_verify_grain_and_export.py)

Implement automated grain verification assertions before exporting clean CSV or Parquet files to stakeholders, preventing silent multi-million dollar duplication errors.

---

## The Complete Python Script

Below is the complete script contained in [`05_verify_grain_and_export.py`](./05_verify_grain_and_export.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Verify Grain and Clean Hand-Off
License: MIT
"""

import pandas as pd
import sys

def verify_grain(df: pd.DataFrame, key_columns: list) -> bool:
    """Ensure key_columns uniquely identify each row (no accidental fan-out)."""
    total_rows = len(df)
    unique_keys = len(df.drop_duplicates(subset=key_columns))
    
    if total_rows != unique_keys:
        duplicates_count = total_rows - unique_keys
        print(f"❌ Grain violation! Found {duplicates_count} duplicate rows for keys {key_columns}")
        return False
        
    print(f"✅ Grain verified: {total_rows} rows uniquely identified by {key_columns}")
    return True

# Construct sample dataset
orders_df = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 1, 2, 3, 4],
    "order_total": [1450.00, 820.00, 3100.00, 450.00, 1980.00],
    "status": ["completed", "completed", "completed", "pending", "completed"]
})

# Verify primary key grain
if not verify_grain(orders_df, ["order_id"]):
    sys.exit(1)

# Export clean artifacts
orders_df.to_csv("clean_orders.csv", index=False)
orders_df.to_parquet("clean_orders.parquet", index=False)
print("📦 Clean datasets exported to clean_orders.csv and clean_orders.parquet")
```

---

## Why Grain Verification is Non-Negotiable

1. **Fan-Out Prevention:** If an upstream `JOIN` accidentally produces a 1:N relationship instead of 1:1, order totals get duplicated. Without grain validation, dashboards report phantom revenue.
2. **Parquet vs CSV for Hand-Off:** Parquet stores column data in columnar binary format with embedded metadata types. Downstream consumers don't have to re-parse date formats or float precision.

---

## How to Run

```bash
python3 python/05_verify_grain_and_export.py
```

👉 Next: [Part 6: Python and SQL Together](./06_python_and_sql_together.md)
