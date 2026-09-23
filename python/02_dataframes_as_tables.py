"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: DataFrames as Tables
License: MIT
"""

import pandas as pd
import numpy as np

# 1. Creating a DataFrame from raw records (analagous to an SQL table)
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

print("
=== Summary Statistics (like SQL AVG/MIN/MAX) ===")
print(df.describe())

# 3. Viewing Top Rows (like SELECT * FROM orders LIMIT 3)
print("
=== Head (Limit 3) ===")
print(df.head(3))
