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
