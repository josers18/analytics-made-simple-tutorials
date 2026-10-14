# How to let Claude or ChatGPT query your data warehouse safely through MCP

> Companion code for the Analytics Made Simple guide: [How to let Claude or ChatGPT query your data warehouse safely through MCP](https://analyticsmadesimple.com/tutorials/mcp-data-warehouse-read-only-ai-access/)

> Raw Script: [`04_read_only_warehouse_mcp_server.py`](./04_read_only_warehouse_mcp_server.py)

A small MCP server that lets Claude (or any MCP client) query a Postgres database through the AI's own **read-only login**. The login is the real protection. The server adds a second layer: one `SELECT` at a time, a 200-row cap, and one log line per query in `ai_queries.jsonl`.

Built and tested on October 14, 2026 with Postgres 18, the MCP Python SDK 2.3.0 (where `FastMCP` is now `MCPServer`) and psycopg 3.3.

## How it flows

```text
you ──question──> Claude ──SQL──> MCP server ──check_sql()──> Postgres (as ai_reader)
                                     │                              │
                                     └── ai_queries.jsonl           └── grants: SELECT on one view only
```

## 1. Practice data

```sql
CREATE TABLE customers (customer_id int PRIMARY KEY, name text, email text, region text);
CREATE TABLE orders (order_id int PRIMARY KEY, customer_id int REFERENCES customers, order_date date, amount numeric(10,2));
INSERT INTO customers VALUES
 (1,'Ana Ortiz','ana@example.com','West'),(2,'Ben Cole','ben@example.com','East'),
 (3,'Chen Li','chen@example.com','West'),(4,'Dee Park','dee@example.com','North');
INSERT INTO orders VALUES
 (101,1,'2026-09-02',120.00),(102,2,'2026-09-05',80.50),(103,3,'2026-09-11',42.00),
 (104,1,'2026-09-19',65.25),(105,4,'2026-09-23',210.00),(106,3,'2026-10-01',99.99);
```

## 2. The AI's read-only login

```sql
-- 1. A view with only what the AI needs: no names, no emails.
CREATE VIEW sales_by_region AS
SELECT c.region, o.order_date, o.amount
FROM orders o JOIN customers c USING (customer_id);

-- 2. A login just for the AI, read-only, with a 10-second query limit.
CREATE ROLE ai_reader LOGIN PASSWORD 'change-me';
ALTER ROLE ai_reader SET default_transaction_read_only = on;
ALTER ROLE ai_reader SET statement_timeout = '10s';

-- 3. It may read the view and nothing else.
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM ai_reader;
GRANT USAGE ON SCHEMA public TO ai_reader;
GRANT SELECT ON sales_by_region TO ai_reader;
```

## 3. Four tries as `ai_reader`

```sql
SELECT region, count(*) AS orders, sum(amount) AS revenue FROM sales_by_region GROUP BY region ORDER BY revenue DESC;
SELECT email FROM customers;
UPDATE orders SET amount = 0;
SELECT pg_sleep(15);
```

```text
 region | orders | revenue 
--------+--------+---------
 West   |      4 |  327.24
 North  |      1 |  210.00
 East   |      1 |   80.50
(3 rows)

psql:tests.sql:2: ERROR:  permission denied for table customers
psql:tests.sql:3: ERROR:  cannot execute UPDATE in a read-only transaction
psql:tests.sql:4: ERROR:  canceling statement due to statement timeout
```

The read-only switch can be turned off by the login itself, but grants still block the change:

```sql
SET default_transaction_read_only = off;
UPDATE orders SET amount = 0;
```

```text
SET
psql:bypass.txt:2: ERROR:  permission denied for table orders
```

## 4. The MCP server

```python
# Analytics Made Simple (analyticsmadesimple.com)
# Tutorial: How to let Claude or ChatGPT query your data warehouse safely through MCP (https://analyticsmadesimple.com/tutorials/mcp-data-warehouse-read-only-ai-access/)
# License: MIT
#
# A small MCP server that lets an AI query a Postgres database through a read-only login.
# The database role does the real protection; this server adds a second layer:
# one SELECT at a time, a row cap, and a log line for every query.
#
# Needs: pip install mcp "psycopg[binary]"   (mcp 2.x)
# Set DATABASE_URL to the AI's own read-only login, for example:
#   export DATABASE_URL="postgresql://ai_reader:change-me@localhost:5432/shop"
import json
import os
import re
import time

import psycopg
from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations

DATABASE_URL = os.environ.get("DATABASE_URL", "")
MAX_ROWS = 200
LOG_FILE = "ai_queries.jsonl"

server = MCPServer("read-only-warehouse")


def check_sql(sql):
    """Return a reason to refuse the query, or None if it may run."""
    s = sql.strip().rstrip(";").strip()
    if not s:
        return "empty query"
    if ";" in s:
        return "one statement at a time"
    if not re.match(r"(?is)^(select|with)\b", s):
        return "only SELECT queries are allowed"
    if re.search(r"(?i)\b(insert|update|delete|drop|alter|create|grant|truncate|copy|set)\b", s):
        return "query contains a word that changes data or settings"
    return None


def log(entry):
    entry["time"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")


@server.tool(annotations=ToolAnnotations(read_only_hint=True))
def list_views() -> dict:
    """List the views this assistant may query, with their columns."""
    with psycopg.connect(DATABASE_URL) as conn:
        rows = conn.execute(
            "SELECT table_name, column_name, data_type FROM information_schema.columns "
            "WHERE table_schema = 'public' AND table_name IN "
            "(SELECT table_name FROM information_schema.role_table_grants "
            " WHERE grantee = current_user AND privilege_type = 'SELECT') "
            "ORDER BY table_name, ordinal_position"
        ).fetchall()
    views = {}
    for table, column, dtype in rows:
        views.setdefault(table, []).append(f"{column} ({dtype})")
    return views


@server.tool(annotations=ToolAnnotations(read_only_hint=True))
def run_query(sql: str) -> dict:
    """Run one read-only SELECT and return at most 200 rows."""
    reason = check_sql(sql)
    if reason:
        log({"sql": sql, "ok": False, "error": reason})
        return {"error": f"Refused: {reason}."}
    try:
        with psycopg.connect(DATABASE_URL) as conn:
            conn.read_only = True
            cur = conn.execute(f"SELECT * FROM ({sql.strip().rstrip(';')}) AS q LIMIT {MAX_ROWS + 1}")
            cols = [d.name for d in cur.description]
            rows = cur.fetchall()
    except psycopg.Error as e:
        log({"sql": sql, "ok": False, "error": str(e).strip()})
        return {"error": str(e).strip()}
    truncated = len(rows) > MAX_ROWS
    rows = [[str(v) for v in r] for r in rows[:MAX_ROWS]]
    log({"sql": sql, "ok": True, "rows": len(rows), "truncated": truncated})
    return {"columns": cols, "rows": rows, "truncated": truncated}


if __name__ == "__main__":
    if not DATABASE_URL:
        raise SystemExit("Set DATABASE_URL to the AI's read-only login first.")
    server.run()  # stdio, for Claude Desktop or Claude Code
```

### What each part does

| Part | What it does |
|---|---|
| `check_sql()` | Refuses empty input, more than one statement, anything not starting with `SELECT`/`WITH`, and queries containing words that change data or settings. A rough second layer: the database grants are the real wall. |
| `run_query` | Wraps the query in `SELECT * FROM (...) LIMIT 201`, opens a read-only connection, returns at most 200 rows and a `truncated` flag, and logs the call. |
| `list_views` | Lists only the views the login was granted, so the AI knows what it may ask about. |
| `read_only_hint=True` | Tells MCP clients the tools only read. Clients may use it to skip confirmations; it protects nothing by itself. |

## 5. Test client (real output)

```python
import asyncio, json, os, sys
from mcp import Client, StdioServerParameters

params = StdioServerParameters(command=sys.executable, args=["04_read_only_warehouse_mcp_server.py"],
                               env={**os.environ, "DATABASE_URL": "postgresql://ai_reader@/shop?host=/tmp&port=5433"})
TRIES = [
    ("list_views", {}),
    ("run_query", {"sql": "SELECT region, count(*) AS orders, sum(amount) AS revenue FROM sales_by_region GROUP BY region ORDER BY revenue DESC"}),
    ("run_query", {"sql": "SELECT email FROM customers"}),
    ("run_query", {"sql": "DELETE FROM orders"}),
    ("run_query", {"sql": "SELECT 1; DROP TABLE orders"}),
]
async def main():
    async with Client(params) as c:
        tools = await c.list_tools()
        print("tools:", [(t.name, t.annotations.read_only_hint if t.annotations else None) for t in tools.tools])
        for name, args in TRIES:
            r = await c.call_tool(name, args)
            out = r.structured_content if r.structured_content else r.content[0].text
            print(f"\n{name} {args.get('sql','')}\n-> {json.dumps(out)}")
asyncio.run(main())
```

```text
tools: [('list_views', True), ('run_query', True)]
run_query SELECT region, ... FROM sales_by_region ...  -> 3 rows (West 327.24, North 210.00, East 80.50)
run_query SELECT email FROM customers                    -> permission denied for table customers
run_query DELETE FROM orders                             -> Refused: only SELECT queries are allowed.
run_query SELECT 1; DROP TABLE orders                    -> Refused: one statement at a time.
```

`ai_queries.jsonl` after the run:

```json
{"sql": "SELECT region, count(*) AS orders, sum(amount) AS revenue FROM sales_by_region GROUP BY region ORDER BY revenue DESC", "ok": true, "rows": 3, "truncated": false, "time": "2026-10-14T16:27:26"}
{"sql": "SELECT email FROM customers", "ok": false, "error": "permission denied for table customers", "time": "2026-10-14T16:27:26"}
{"sql": "DELETE FROM orders", "ok": false, "error": "only SELECT queries are allowed", "time": "2026-10-14T16:27:26"}
{"sql": "SELECT 1; DROP TABLE orders", "ok": false, "error": "one statement at a time", "time": "2026-10-14T16:27:26"}
```

## How to run

```bash
pip install mcp "psycopg[binary]"
export DATABASE_URL="postgresql://ai_reader:change-me@localhost:5432/shop"
python3 04_read_only_warehouse_mcp_server.py      # stdio server

# add it to Claude Code
claude mcp add warehouse \
  -e DATABASE_URL="postgresql://ai_reader:change-me@localhost:5432/shop" \
  -- python3 04_read_only_warehouse_mcp_server.py
```

`claude mcp list` showed the server as connected on October 14, 2026.

## Next

- [How to check AI-written SQL before you ship it](https://analyticsmadesimple.com/tutorials/how-to-check-ai-written-sql/)
