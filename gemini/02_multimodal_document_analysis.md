# Gemini Tutorial 2: Multimodal Document & Invoice Analysis

> **Official Companion Guide for [Analytics Made Simple: Gemini Multimodal](https://analyticsmadesimple.com/series/gemini/)**
> Raw Script: [`02_multimodal_document_analysis.py`](./02_multimodal_document_analysis.py)

Extract structured tabular records from receipts, scanned invoices, and dashboard screenshots using Gemini's native multimodal vision capabilities.

---

## The Complete Python Script

Below is the code contained in [`02_multimodal_document_analysis.py`](./02_multimodal_document_analysis.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Multimodal Image & Document Analysis with Gemini
Series: Gemini Everyday & Multimodal
License: MIT
"""

def build_multimodal_extraction_prompt(fields_to_extract: list[str]) -> str:
    """Builds a schema-enforced prompt for visual document inspection."""
    return f"""You are an automated document parsing engine.
Inspect the attached invoice / screenshot image carefully.

Extract the following required fields:
{fields_to_extract}

### Output Rules:
- Return ONLY valid JSON.
- If a field is blurred, obscured, or missing, set its value to null. Never guess numbers.
- Transcribe currency values as pure decimal floats (e.g. 1450.00, not '$1,450.00').
"""

if __name__ == "__main__":
    fields = ["invoice_number", "vendor_name", "invoice_date", "subtotal", "tax_amount", "total_amount"]
    prompt = build_multimodal_extraction_prompt(fields)
    print("=== Compiled Multimodal Document Prompt ===")
    print(prompt)
```

---

## How to Run

```bash
python3 gemini/02_multimodal_document_analysis.py
```

👉 Next: [Part 3: Gemini CLI & Antigravity Terminal Workflows](./03_gemini_cli_antigravity_workflows.md)
