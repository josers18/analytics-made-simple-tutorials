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

print("
=== Standardized Leads ===")
print(raw_leads[["lead_id", "company_standard", "channel_clean"]])
