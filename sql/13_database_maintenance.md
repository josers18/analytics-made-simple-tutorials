# SQL Tutorial 13: Strategies for Maintenance and Optimization

> **Official Companion Guide for [Analytics Made Simple: SQL Tutorial 13 - Maintenance](https://analyticsmadesimple.com/tutorials/sql-tutorial-13-strategies-for-maintenance-and-optimization/)**
> Raw Script: [`13_database_maintenance.sql`](./13_database_maintenance.sql)

High-performance databases require ongoing maintenance: statistics refreshing, fragmentation vacuuming, and automated integrity validation.

---

## The Complete SQL Script

Below is the complete SQL script contained in [`13_database_maintenance.sql`](./13_database_maintenance.sql):

```sql
-- Analytics Made Simple (analyticsmadesimple.com)
-- Tutorial 13: Strategies for Maintenance and Optimization (https://analyticsmadesimple.com/tutorials/sql-tutorial-13-strategies-for-maintenance-and-optimization/)
-- License: MIT

-- 1. Query Optimizer Statistics Gathering
ANALYZE;

-- 2. Database Compaction and Page Defragmentation
VACUUM;

-- 3. Integrity Verification Check
PRAGMA integrity_check;
PRAGMA foreign_key_check;
```

---

## Routine Maintenance Checklist

| Operation | Command | Purpose |
|:---|:---|:---|
| **Update Statistics** | `ANALYZE;` | Updates internal distribution statistics so the query planner makes optimal index decisions. |
| **Reclaim Storage** | `VACUUM;` | Rebuilds the database file, defragmenting pages and shrinking disk usage after heavy deletes. |
| **Data Integrity** | `PRAGMA integrity_check;` | Verifies B-Tree page consistency and reports any corruption errors. |
| **Referential Integrity** | `PRAGMA foreign_key_check;` | Verifies that no child tables have orphaned foreign key pointers. |

---

## How to Run

```bash
sqlite3 ams_playground.db < sql/13_database_maintenance.sql
```

🎓 **Congratulations!** You have completed all 14 parts of the SQL Mastery Curriculum.
Explore the next curriculum tracks:
* [Python for Analytics & Data Engineering](../python/README.md)
* [TypeSafe AI & Decision Engines](../typesafe-ai/README.md)
