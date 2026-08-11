---
name: sql-expert
description: "Expert SQL query writing, optimization, and database schema design with support for PostgreSQL, MySQL, SQLite, and SQL Server. Use when working with databases for: (1) Writing complex SQL queries with joins, subqueries, and window functions, (2) Optimizing slow queries and analyzing execution plans, (3) Designing database schemas with proper normalization, (4) Creating indexes and improving query performance, (5) Writing migrations and handling schema changes, (6) Debugging SQL errors and query issues"
model: inherit
---

# SQL Expert

Expert guidance for writing, optimizing, and managing SQL databases across PostgreSQL, MySQL, SQLite, and SQL Server.

## Specialized Agents

Specialized personas for database roles. Load these from `agents/` to provide expert context.

| Agent | Role | Focus |
|-------|------|-------|
| **sql-pro** | SQL Expert | Query optimization, schema design, migrations, indexing. |

## When to Use

Apply this skill when working with databases for:
- Writing complex SQL queries (JOINs, CTEs, Window Functions)
- Optimizing slow queries and analyzing execution plans
- Designing normalized database schemas (1NF, 2NF, 3NF)
- Creating and managing effective indexes
- Writing safe database migrations
- Debugging SQL errors and performance issues
- Handling transactions and isolation levels

## Step 1: Detect Database Environment

**Always check the database type and version before providing SQL or optimization advice.**

```bash
# For MySQL
mysql --version
# For PostgreSQL
psql --version
# For SQLite
sqlite3 --version
```

## Core Directives

### MUST DO

- Use **Parameterized Queries** to prevent SQL injection (MANDATORY)
- Wrap multi-step data modifications in **Transactions**
- Index all **Foreign Keys** and columns used in `WHERE`, `JOIN`, and `ORDER BY`
- Always use `EXPLAIN ANALYZE` to identify query bottlenecks
- Include `created_at` and `updated_at` timestamps on all tables
- Use `DECIMAL` for financial data, never `FLOAT` or `DOUBLE`
- Follow the **Rule of Three** for normalization (don't over-normalize simple data)

### MUST NOT DO

- Use `SELECT *` on large tables or production queries
- Perform destructive operations (DELETE/UPDATE) without a `WHERE` clause
- Use functions on indexed columns in `WHERE` clauses (e.g., `WHERE LOWER(email)`)
- Share database schemas between microservices
- Use sequential IDs in public-facing URLs (prefer UUIDs)
- Ignore NULL handling (remember: `NULL = NULL` is UNKNOWN/NULL)

## Category Index — When to Load Which Reference

| # | Category | Impact | Load when… | Reference | Prefix |
|--:|----------|:------:|------------|-----------|--------|
| 1 | Optimization | CRITICAL | Fixing slow queries, analyzing EXPLAIN plans | [`references/query-optimization.md`](references/query-optimization.md) | `qry-` |
| 2 | Best Practices | CRITICAL | Designing schemas, naming conventions, security | [`references/best-practices.md`](references/best-practices.md) | `schema-` |
| 3 | Indexing Strategy | CRITICAL | Creating indexes, composite index design, JSON column indexing | [`references/indexes-performance.md`](references/indexes-performance.md) | `idx-` |
| 4 | Advanced Patterns | HIGH | Using CTEs, Window Functions, JSON operations | [`references/advanced-patterns.md`](references/advanced-patterns.md) | `qry-` |
| 5 | Common Pitfalls | MEDIUM | Debugging common SQL errors or anti-patterns | [`references/common-pitfalls.md`](references/common-pitfalls.md) | `txn-` |

## Rule Index

All rules live in [`rules/core-directives.md`](rules/core-directives.md) in `Context` / `Rule` / `Avoid` form. Cite the ids in reviews.

### 1. Query Optimization (`qry-`) — CRITICAL
`qry-explain-before-tuning` · `qry-sargable-predicates` · `qry-no-select-star` · `qry-exists-over-count` · `qry-set-based-not-row-by-row` · `qry-join-over-correlated-subquery`

### 2. Schema Design (`schema-`) — CRITICAL
`schema-normalize-then-denormalize` · `schema-narrowest-correct-type` · `schema-timestamps-utc` · `schema-constraints-in-the-database`

### 3. Indexing Strategy (`idx-`) — CRITICAL
`idx-foreign-keys` · `idx-composite-column-order` · `idx-leftmost-prefix` · `idx-cover-the-hot-query` · `idx-json-and-fulltext`

### 4. Transactions & Safe Change (`txn-`) — CRITICAL
`txn-parameterized-statements` · `txn-short-transactions` · `txn-atomic-modifications` · `txn-zero-downtime-migrations`

## Validation Checklist

- [ ] Query uses parameterized inputs (no concatenation)
- [ ] `EXPLAIN ANALYZE` shows index usage for all large table filters
- [ ] Transactions wrap all multi-table or multi-step writes
- [ ] All foreign keys are indexed
- [ ] Financial data uses `DECIMAL` types
- [ ] Schema follows at least 3NF (unless denormalization is justified)
- [ ] No `SELECT *` used in production-grade queries
- [ ] NULL values are handled correctly in logic and filters

## External References

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQL Zoo (Tutorials)](https://sqlzoo.net)
- [Use The Index, Luke](https://use-the-index-luke.com)
