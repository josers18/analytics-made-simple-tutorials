# AI Engineering: Prompt Patterns for Data Work

> **Official Companion Guide for [Analytics Made Simple: Prompt Patterns for Data Work](https://analyticsmadesimple.com/tutorials/)**
> Raw Script: [`01_prompt_patterns_for_data.py`](./01_prompt_patterns_for_data.py)

How to construct constrained, non-hallucinating system prompts for text-to-SQL and analytical extraction.

---

## The Complete Python Script

Below is the complete script contained in [`01_prompt_patterns_for_data.py`](./01_prompt_patterns_for_data.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Prompt Patterns for Data Work
Canonical Article: https://analyticsmadesimple.com/tutorials/
License: MIT
"""

def build_sql_generator_prompt(schema_ddl: str, user_question: str) -> str:
    """Construct a constrained, deterministic prompt for SQL generation."""
    return f"""You are assisting an analytics engineer. Draft executable, standard ANSI SQL for human review.

### Available Database Schema:
{schema_ddl}

### Strict Generation Rules:
1. Use ONLY the tables and columns explicitly defined in the schema above.
2. If a required calculation cannot be fulfilled by the schema, state "INSUFFICIENT_SCHEMA_ERROR" rather than hallucinating table or column names.
3. Use explicit column projections; NEVER output 'SELECT *'.
4. Wrap all identifiers in standard lowercase formatting.
5. Return ONLY executable SQL inside standard markdown code blocks, followed by a 1-sentence explanation of the join logic.

### User Business Request:
"{user_question}"
"""

if __name__ == "__main__":
    sample_schema = """
    CREATE TABLE customers (customer_id INT, name TEXT, region TEXT);
    CREATE TABLE orders (order_id INT, customer_id INT, order_date DATE, order_total DECIMAL);
    """
    prompt = build_sql_generator_prompt(sample_schema, "Show me total revenue by region for completed orders in Q1 2025.")
    print("=== Generated Constrained System Prompt ===")
    print(prompt)
```

---

## The 5 Rules for Reliable Text-to-SQL

1. **Closed-World Assumption:** Explicitly instruct the model to use *only* the provided schema.
2. **Explicit Failure Mode:** Give the LLM an escape hatch (`INSUFFICIENT_SCHEMA_ERROR`). Without an explicit error token, models hallucinate columns like `customer_address` or `profit_margin`.
3. **No Wildcard Projections:** Ban `SELECT *` in the prompt rules.
4. **Structured Formatting:** Require standardized markdown code blocks.
5. **Logic Verification:** Demand a single-sentence explanation of join paths to make human review instant.

---

## How to Run

```bash
python3 ai-engineering/01_prompt_patterns_for_data.py
```

👉 Next: [Part 2: Universal LLM API Client](./02_llm_api_unified_client.md)
