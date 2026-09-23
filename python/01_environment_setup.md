# Python Tutorial 1: Environment Setup & Quickstart

> **Official Companion Guide for [Analytics Made Simple: Python Setup](https://analyticsmadesimple.com/tutorials/)**

Establish a modern, isolated Python analytics environment with pandas, numpy, and pyarrow.

---

## 1. Virtual Environment Installation

```bash
# 1. Create a dedicated virtual environment
python3 -m venv venv

# 2. Activate virtual environment
# macOS / Linux:
source venv/bin/activate
# Windows:
# .\venv\Scripts\activate

# 3. Upgrade pip and install core analytics libraries
pip install --upgrade pip
pip install pandas numpy pyarrow
```

---

## 2. Environment Verification Script

Create and run a quick verification script to confirm your setup:

```python
import pandas as pd
import numpy as np
import pyarrow as pa

print("=== Analytics Environment Verified ===")
print(f"Pandas version:  {pd.__version__}")
print(f"NumPy version:   {np.__version__}")
print(f"PyArrow version: {pa.__version__}")
```

Expected Output:
```text
=== Analytics Environment Verified ===
Pandas version:  2.2.x
NumPy version:   1.26.x
PyArrow version: 15.0.x
```

👉 Next: [Part 2: DataFrames as Tables](./02_dataframes_as_tables.md)
