#!/usr/bin/env python3
"""
Verify Grain and Export Reliable Hand-Offs in Pandas
Tutorial: https://analyticsmadesimple.com/analytics/pandas-export-and-hand-off/
Key Term: https://analyticsmadesimple.com/key-terms/what-is-grain-in-data/
"""

import pandas as pd

def main():
    print("Loading raw order line transactions...")
    # Sample data at order-line grain
    data = [
        {"order_id": 1001, "line_id": 1, "customer_id": "C7", "sku": "MUG", "line_amount": 30.00},
        {"order_id": 1001, "line_id": 2, "customer_id": "C7", "sku": "TEA", "line_amount": 50.00},
        {"order_id": 1002, "line_id": 1, "customer_id": "C7", "sku": "MUG", "line_amount": 20.00},
        {"order_id": 1003, "line_id": 1, "customer_id": "C9", "sku": "COFFEE", "line_amount": 15.00}
    ]
    df = pd.DataFrame(data)

    # 1. Assert Grain at line level
    line_keys = ["order_id", "line_id"]
    is_unique_line = df.duplicated(subset=line_keys).sum() == 0
    assert is_unique_line, "Grain assertion failed: Duplicate order lines detected!"
    print(f"PASS: Line grain unique on {line_keys}")

    # 2. Aggregate cleanly to Order grain
    order_summary = (
        df.groupby(["order_id", "customer_id"], as_index=False)
        .agg(
            total_revenue=("line_amount", "sum"),
            item_count=("line_id", "count")
        )
    )

    # 3. Assert Grain at order level
    is_unique_order = order_summary.duplicated(subset=["order_id"]).sum() == 0
    assert is_unique_order, "Grain assertion failed: Duplicate orders detected!"
    print(f"PASS: Order grain unique on ['order_id']")
    print("\nOrder Summary:")
    print(order_summary)

if __name__ == "__main__":
    main()
