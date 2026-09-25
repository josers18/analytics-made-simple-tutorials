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

# Export clean artifacts. CSV always works. Parquet needs pyarrow or fastparquet.
orders_df.to_csv("clean_orders.csv", index=False)
try:
    orders_df.to_parquet("clean_orders.parquet", index=False)
except ImportError:
    print("CSV written to clean_orders.csv. Parquet needs pyarrow: pip install pyarrow")
else:
    print("Clean datasets exported to clean_orders.csv and clean_orders.parquet")
