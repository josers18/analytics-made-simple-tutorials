# Claude Code: The Data Analyst Workflow Guide

> **Official Companion Guide for [Analytics Made Simple: Claude Code for Data Work](https://analyticsmadesimple.com/tutorials/)**

How modern data analysts and analytics engineers pair with Claude Code to accelerate everyday exploratory work.

---

## 1. Schema Auditing
Ask Claude Code to inspect your schema files and detect missing constraints:
```bash
claude "Inspect sql/01_playground_setup.sql and flag any foreign keys lacking supporting B-tree indexes."
```

## 2. Converting SQL into Pandas
```bash
claude "Translate the window function query in sql/10_advanced_ctes_window_functions.sql into idiomatic pandas code using groupby and transform."
```

## 3. Automated Documentation
```bash
claude "Scan all SQL queries in the sql/ folder and generate a clean Markdown table summarizing input tables, output grain, and key aggregations."
```
