# Rules for SQL & Schema Design

Actionable directives for query optimization, schema design, indexing, and safe data modification.

Target engines: **PostgreSQL 17**, **MySQL 8.4 LTS**, **SQL Server 2022**, SQLite. Engine-specific behaviour is called out where it diverges.

Cite these ids in reviews (`qry-no-select-star`, `idx-leftmost-prefix`, `txn-short-transactions`) so feedback is traceable back to the source rule.

## 1. Query Optimization (`qry-`)

### `qry-explain-before-tuning`
- **Context:** Any query suspected of being slow.
- **Rule:** Read the plan before changing anything. `EXPLAIN (ANALYZE, BUFFERS)` on PostgreSQL, `EXPLAIN ANALYZE` on MySQL 8.0+, `SET STATISTICS IO, TIME ON` plus the actual plan on SQL Server. Compare estimated versus actual rows — a large divergence means stale statistics, not a missing index.
- **Avoid:** Adding indexes by intuition. Also avoid tuning against `EXPLAIN` alone: it shows the plan, not the row counts and buffer reads that identify the real cost.

### `qry-sargable-predicates`
- **Context:** `WHERE` and `JOIN` conditions.
- **Rule:** Keep the indexed column bare on one side of the comparison so the index can be used. Transform the constant instead of the column.
- **Avoid:** `WHERE YEAR(created_at) = 2025` → use `created_at >= '2025-01-01' AND created_at < '2026-01-01'`. Same for `LOWER(email) = ?` (use a case-insensitive collation or an expression index), leading-wildcard `LIKE '%x'`, and implicit type coercion between a `varchar` column and an integer parameter.

### `qry-no-select-star`
- **Context:** Production queries and views.
- **Rule:** List the columns you need. This enables covering indexes, reduces I/O and network transfer, and stops a new `TEXT`/`BLOB` column from silently slowing every existing query.
- **Avoid:** `SELECT *` in application code, in views, and especially inside `EXISTS` subqueries where no column is needed at all. Ad-hoc exploration is fine.

### `qry-exists-over-count`
- **Context:** Checking whether any row matches.
- **Rule:** Use `EXISTS`, which stops at the first match. `COUNT(*)` scans every matching row to produce a number you then compare to zero.
- **Avoid:** `IF (SELECT COUNT(*) FROM orders WHERE user_id = ?) > 0`. Also avoid `COUNT(*)` for pagination totals on large tables — use keyset pagination or an approximate count (`pg_class.reltuples`).

### `qry-set-based-not-row-by-row`
- **Context:** Bulk updates and inserts.
- **Rule:** Express the operation as one statement over a set. `INSERT … SELECT`, `UPDATE … FROM`, `MERGE`, and multi-row `VALUES` beat a loop issuing one statement per row by orders of magnitude.
- **Avoid:** Application loops calling `execute()` per row (the N+1 write), and cursors where a join would do.

### `qry-join-over-correlated-subquery`
- **Context:** Subqueries referencing the outer row.
- **Rule:** Prefer a join or a lateral join when a correlated subquery runs per row. Check the plan — modern optimizers unnest many correlated subqueries, so verify rather than assume.
- **Avoid:** `SELECT (SELECT MAX(created_at) FROM orders o WHERE o.user_id = u.id) FROM users u` over a large `users` table without confirming the plan.

## 2. Schema Design (`schema-`)

### `schema-normalize-then-denormalize`
- **Context:** Table design.
- **Rule:** Start at third normal form. Denormalize deliberately, for a measured read pattern, and document what keeps the copy consistent.
- **Avoid:** Repeating groups (`phone1`, `phone2`, `phone3`), comma-separated lists in a column, and entity-attribute-value tables used as a general-purpose schema.

### `schema-narrowest-correct-type`
- **Context:** Column types.
- **Rule:** Choose the narrowest type that holds every legal value. Money as integer minor units or `NUMERIC`/`DECIMAL` — never `FLOAT`. Identifiers as `BIGINT` or `UUID`, chosen deliberately. Enumerated states as a native enum or a lookup table with a foreign key.
- **Avoid:** `VARCHAR(255)` for everything, floats for currency, storing JSON blobs for fields you filter or join on, and `TEXT` columns holding numbers.

### `schema-timestamps-utc`
- **Context:** Temporal columns.
- **Rule:** Store instants as `TIMESTAMPTZ` (PostgreSQL) / `TIMESTAMP` with an explicit UTC session (MySQL) / `DATETIMEOFFSET` (SQL Server). Convert to local time at the presentation edge only.
- **Avoid:** Naive local timestamps, and `TIMESTAMP` on MySQL for dates beyond 2038. Keep `created_at`/`updated_at` on every mutable table — their absence makes incidents un-investigable.

### `schema-constraints-in-the-database`
- **Context:** Data integrity.
- **Rule:** Enforce invariants where the data lives: `NOT NULL`, `UNIQUE`, `CHECK`, and foreign keys with explicit `ON DELETE` behaviour. Application validation is a user-experience layer, not a guarantee — jobs, migrations, and consoles bypass it.
- **Avoid:** Nullable columns as the default, foreign keys omitted "for performance" (they are cheap and the missing index is the real cost), and `ON DELETE CASCADE` chosen without considering what it will remove.

## 3. Indexing Strategy (`idx-`)

### `idx-foreign-keys`
- **Context:** Foreign key columns.
- **Rule:** Index every foreign key column. PostgreSQL and MySQL/InnoDB do not create the child-side index automatically for all cases, and without it every parent delete or update scans the child table, holding locks while it does.
- **Avoid:** Assuming the constraint implies an index. MySQL/InnoDB creates one for `FOREIGN KEY`; PostgreSQL does not.

### `idx-composite-column-order`
- **Context:** Multi-column indexes.
- **Rule:** Order columns equality-first, then range, then the columns needed for `ORDER BY`. One well-ordered composite index usually replaces several single-column ones.
- **Avoid:** A separate index per column and hoping the engine combines them. Bitmap/index merges are far slower than one composite index.

### `idx-leftmost-prefix`
- **Context:** Using a composite index.
- **Rule:** A composite index on `(a, b, c)` serves predicates on `a`, `(a, b)`, and `(a, b, c)`. A query filtering only on `b` cannot use it.
- **Avoid:** Creating `(a, b)` and `(a)` — the second is redundant. Check the leftmost column matches the query's most selective equality predicate before adding an index at all.

### `idx-cover-the-hot-query`
- **Context:** A frequently run query that is still slow after indexing the predicate.
- **Rule:** Add the selected columns to the index so it can be answered without touching the table — `INCLUDE` on PostgreSQL and SQL Server, extra trailing key columns on MySQL. Confirm with an index-only scan in the plan.
- **Avoid:** Covering every query. Each index slows writes, consumes memory, and must be maintained; add them for measured hot paths only. Drop unused indexes — `pg_stat_user_indexes`, `sys.dm_db_index_usage_stats`, `performance_schema` show which are never read.

### `idx-json-and-fulltext`
- **Context:** Querying inside JSON or searching text.
- **Rule:** For JSON, index the extracted expression: a `GIN` index on `jsonb` (PostgreSQL), a generated column plus a normal index (MySQL), or a computed persisted column (SQL Server). For text search use the engine's full-text feature (`tsvector` + `GIN`, `FULLTEXT`), not `LIKE '%term%'`.
- **Avoid:** Filtering on a JSON path with no supporting index — it is a full scan with a function call per row. If a field is filtered often, it should be a column.

## 4. Transactions & Safe Change (`txn-`)

### `txn-parameterized-statements`
- **Context:** Any query containing a value from outside the process.
- **Rule:** Bind values as parameters so they never become part of the parsed statement. Identifiers (table, column, sort direction) cannot be bound — validate them against an allow-list.
- **Avoid:** String concatenation or interpolation into SQL, and client-side emulated prepares (`PDO::ATTR_EMULATE_PREPARES = false`). Escaping functions are not equivalent to binding.

### `txn-short-transactions`
- **Context:** Transaction scope.
- **Rule:** Open the transaction as late as possible, commit as early as possible, and keep only database work inside it. Order writes to shared rows consistently across the codebase to avoid deadlocks, and retry on the engine's deadlock/serialization error.
- **Avoid:** HTTP calls, queue publishes, email sends, or user interaction inside a transaction. Side effects that cannot roll back belong after the commit — use an outbox table if they must be atomic with the write.

### `txn-atomic-modifications`
- **Context:** Read-modify-write on a shared value.
- **Rule:** Let the database do the arithmetic (`UPDATE accounts SET balance = balance - ? WHERE id = ? AND balance >= ?`) or take an explicit lock (`SELECT … FOR UPDATE`, `UPDLOCK`). Prefer optimistic concurrency with a version column where contention is low.
- **Avoid:** Reading a value into the application, computing, and writing it back without a lock or version check — the classic lost update.

### `txn-zero-downtime-migrations`
- **Context:** Schema changes on a live table.
- **Rule:** Make changes additive and reversible in stages: add a nullable column → backfill in batches → start writing to it → switch reads → drop the old column in a later release. Build indexes without blocking (`CREATE INDEX CONCURRENTLY` on PostgreSQL, `ALGORITHM=INPLACE, LOCK=NONE` on MySQL, `WITH (ONLINE = ON)` on SQL Server Enterprise).
- **Avoid:** Renaming or dropping a column in the same release that changes the code, adding a `NOT NULL` column with a default to a large table without checking whether your engine version rewrites the table, and unbatched `UPDATE`s that lock millions of rows.
