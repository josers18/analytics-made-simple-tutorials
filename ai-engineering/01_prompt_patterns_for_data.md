# Prompt: write SQL only from the schema you were given

> **Official companion for [Analytics Made Simple](https://analyticsmadesimple.com/tutorials/)**

This file is a prompt. Paste it into the model that will draft SQL. It does not connect to a database.

## Paste this

```text
Draft one SQL query for the question at the end. Use only the tables and columns in this schema.
If the schema cannot answer the question, reply INSUFFICIENT_SCHEMA and stop.
Do not write SELECT *. Use lowercase names.
Return the query, then one sentence on how the tables connect.

Schema:
CREATE TABLE customers (customer_id INT, name TEXT, region TEXT);
CREATE TABLE orders (order_id INT, customer_id INT, order_date DATE, order_total DECIMAL, status TEXT);

Question: total revenue by region for completed orders in 2025 Q1.
```

`orders` has `status` and `order_date`, so a completed-order filter is possible. It has no `region` column, so the query has to join `customers`.

## Next

[Call three APIs with the same question](./02_llm_api_unified_client.md)
