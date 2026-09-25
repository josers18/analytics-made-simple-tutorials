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
print("=== High Value Completed Orders ===")
print(high_value_completed)

# 3. Range Filtering (WHERE region IN ('Europe', 'Asia-Pacific'))
international = df[df["region"].isin(["Europe", "Asia-Pacific"])]
print("=== International Orders ===")
print(international)

# 4. Sorting (ORDER BY region ASC, order_total DESC)
sorted_df = df.sort_values(by=["region", "order_total"], ascending=[True, False])
print("=== Sorted DataFrame ===")
print(sorted_df)
