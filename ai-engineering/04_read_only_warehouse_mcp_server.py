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
