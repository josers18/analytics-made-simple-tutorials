# Python Tutorial 4: Standardizing Categories and Names

> **Official Companion Guide for [Analytics Made Simple: Standardizing Categories and Names](https://analyticsmadesimple.com/analytics/standardizing-categories-and-names/)**
> Raw Script: [`04_standardizing_categories_and_names.py`](./04_standardizing_categories_and_names.py)

Clean up human-entered messy strings, normalize casing, strip legal entity suffixes, and map fuzzy categorical channels with deterministic Python pipelines.

---

## The Complete Python Script

Below is the complete script contained in [`04_standardizing_categories_and_names.py`](./04_standardizing_categories_and_names.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Standardizing Categories and Names
License: MIT
"""

import pandas as pd
import re

# Messy operational data
raw_leads = pd.DataFrame({
    "lead_id": [1, 2, 3, 4, 5, 6],
    "company_raw": [" Acme Inc. ", "acme industrial", "Apex Logistics Ltd", "beacon health", "BEACON HEALTH ORG", "Crestview"],
    "channel": ["Organic Search", "organic_search", "Paid-Google", "PAID GOOGLE", "referral", " Referral "]
})

print("=== Raw Unstandardized Leads ===")
print(raw_leads)

# 1. Clean and normalize channel categories
def clean_channel(val):
    if pd.isna(val):
        return "Unknown"
    norm = str(val).strip().lower()
    norm = re.sub(r"[\s\-_]+", " ", norm)
    if "organic" in norm:
        return "Organic Search"
    elif "paid" in norm or "google" in norm:
        return "Paid Search"
    elif "referral" in norm:
        return "Referral"
    return "Other"

raw_leads["channel_clean"] = raw_leads["channel"].apply(clean_channel)

# 2. Standardize company names: strip legal suffixes, whitespace, title case
def clean_company_name(name):
    if pd.isna(name):
        return ""
    n = str(name).strip()
    # Strip common suffixes
    n = re.sub(r"(?i)\b(inc|incorporated|llc|ltd|corp|corporation|org)\b[.]?", "", n)
    # Remove extra internal spaces
    n = re.sub(r"\s+", " ", n).strip()
    return n.title()

raw_leads["company_standard"] = raw_leads["company_raw"].apply(clean_company_name)

print("\n=== Standardized Leads ===")
print(raw_leads[["lead_id", "company_standard", "channel_clean"]])
```

---

## Before & After Cleaning

| lead_id | Raw Company (`company_raw`) | Standardized Company (`company_standard`) | Raw Channel | Clean Channel |
|:---:|:---|:---|:---|:---|
| 1 | ` Acme Inc. ` | **Acme** | `Organic Search` | **Organic Search** |
| 2 | `acme industrial` | **Acme Industrial** | `organic_search` | **Organic Search** |
| 3 | `Apex Logistics Ltd` | **Apex Logistics** | `Paid-Google` | **Paid Search** |
| 4 | `beacon health` | **Beacon Health** | `PAID GOOGLE` | **Paid Search** |
| 5 | `BEACON HEALTH ORG` | **Beacon Health** | `referral` | **Referral** |
| 6 | `Crestview` | **Crestview** | ` Referral ` | **Referral** |

---

## How to Run

```bash
python3 python/04_standardizing_categories_and_names.py
```

👉 Next: [Part 5: Grain Verification and Hand-Off](./05_verify_grain_and_export.md)
