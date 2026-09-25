# Gemini prompt: read an invoice without guessing

> **Official companion for [Learn Gemini](https://analyticsmadesimple.com/series/gemini/)**

This file is a prompt. Attach the invoice image in Gemini, then paste the text. The prompt does not see an image on its own, and there is no Python wrapper that pretends it did.

For a text call you can run locally, use [`01_gemini_api_quickstart.py`](./01_gemini_api_quickstart.py).

## Paste this with the image

```text
Read the attached invoice. Extract only these fields:
invoice_number, vendor_name, invoice_date, subtotal, tax_amount, total_amount

Return JSON.
If a field is blurred, cut off, or absent, set it to null.
Write money as a decimal number, such as 1450.00, not "$1,450.00".
Do not guess a digit you cannot see.
```

## Next

[Gemini CLI notes](./03_gemini_cli_antigravity_workflows.md)
