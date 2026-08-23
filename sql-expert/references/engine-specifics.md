# Engine Specifics — SQLite & SQL Server

PostgreSQL and MySQL behaviour is covered inline throughout the rules and references. This file documents where **SQLite** and **SQL Server** diverge, because their defaults and limits surprise developers who assume Postgres semantics port over.

---

## SQLite

SQLite is an embedded, single-file database: there is no server, no network protocol, and no users. One process writes at a time; many processes may read concurrently (depending on journal mode).

### Connection-time configuration is mandatory

SQLite resets key settings per connection:

```sql
-- Run these on EVERY new connection:
PRAGMA foreign_keys = ON;      -- OFF by default! FKs are silently unenforced otherwise
PRAGMA busy_timeout = 5000;    -- Fail fast instead of hanging on a locked DB
```

- **Rule:** Enable `foreign_keys` on every connection — unlike every other engine, foreign keys are inert until you opt in.
- **Avoid:** Assuming a declared `FOREIGN KEY` does anything without the pragma.

### Journal mode and concurrency

`PRAGMA journal_mode=WAL` (write-ahead logging) allows readers to run concurrently with one writer and survives crashes better than the rollback journal. WAL is persistent: set it once per database file.

- Writers still serialize — SQLite takes a single write lock per database, not per row/page.
- Long-running read transactions block checkpointing and grow the WAL file.
- Use `busy_timeout` to handle writer contention gracefully instead of failing with `SQLITE_BUSY`.

### Type system

SQLite uses type *affinity*, not strict types: a column declared `INTEGER` will happily store text. Since 3.37, declare `CREATE TABLE … STRICT` to enforce real types (`INT`, `TEXT`, `REAL`, `BLOB`, `ANY`).

- There is no dedicated `DATETIME` storage class. Store timestamps as ISO-8601 `TEXT`, Unix epoch `INTEGER`, or Julian `REAL` — pick one convention per schema and stay consistent.
- `DECIMAL` does not exist natively; money is stored as integer minor units or handled carefully with `REAL`. Prefer integer minor units.

### Schema changes are manual rebuilds

`ALTER TABLE` supports rename, add column, and (3.35+) `DROP COLUMN`. Changing a column type, adding constraints, or reordering columns requires the official multi-step procedure: create new table → copy data → drop old → rename → recreate indexes/triggers/views. Foreign-key enforcement must be off during the copy (`PRAGMA foreign_keys=OFF`) and integrity verified after.

### Feature version floor

| Feature | Minimum SQLite |
|---|---|
| UPSERT (`ON CONFLICT DO UPDATE`) | 3.24 |
| Window functions | 3.25 |
| Index on expressions | 3.9 |
| `DROP COLUMN` | 3.35 |
| `RETURNING` | 3.35 |
| STRICT tables | 3.37 |
| `jsonb` type | 3.45 |

Check the runtime version (`SELECT sqlite_version();`) before shipping features from the bottom of this table — OS-bundled SQLite is often years behind.

### Performance practice

- Every foreign key column needs an explicit index — SQLite never auto-indexes them.
- Use `EXPLAIN QUERY PLAN` (not just `EXPLAIN`) to see whether an index is used; run `ANALYZE` so `sqlite_stat1` exists for the planner.
- Partial indexes (`CREATE INDEX … WHERE status = 'active'`) and `WITHOUT ROWID` tables for narrow primary keys are first-class tools here.
- Batch writes inside a transaction: autocommit mode fsyncs per statement, which makes bulk inserts ~100× slower.

### SQL dialect differences to remember

- `LIMIT`/`OFFSET` syntax (no `FETCH FIRST`), `RETURNING` supported, no stored procedures or `ALTER COLUMN`.
- `UPSERT` conflict targets work like PostgreSQL's `ON CONFLICT`.
- String concatenation is `||`, not `+` or `CONCAT()`.

---

## SQL Server (T-SQL)

### Table structure: clustered index or heap

A table is either a **clustered index** (rows physically ordered by the clustered key) or a **heap** (no order). Every table should have a deliberate choice — usually a clustered index on a narrow, ever-increasing unique key. Nonclustered indexes store the clustered key as their row locator.

- `INCLUDE` columns extend a nonclustered index without affecting key ordering — this is the covering-index mechanism (equivalent of PostgreSQL's `INCLUDE`).
- Filtered indexes (`CREATE INDEX … WHERE status = 'active'`) cover hot subsets cheaply.

### Isolation defaults differ from Postgres

Default isolation is `READ COMMITTED` implemented with **locks**: readers block writers and vice versa. Most ORMs expect the Postgres-like behaviour of row versioning:

```sql
ALTER DATABASE mydb SET READ_COMMITTED_SNAPSHOT ON;  -- RCSI: readers don't block writers
ALTER DATABASE mydb SET ALLOW_SNAPSHOT_ISOLATION ON; -- explicit SNAPSHOT transactions
```

- Enabling RCSI is the standard fix for reader/writer blocking in OLTP apps — plan for it at deployment time (it requires exclusive database access for the switch).
- Snapshot-based isolation reads the previous version from `tempdb` — size and monitor `tempdb` accordingly.

### T-SQL syntax that differs

| Concern | T-SQL |
|---|---|
| Row limiting | `SELECT TOP (20) …` or `OFFSET n ROWS FETCH NEXT m ROWS ONLY` (requires `ORDER BY`) |
| Null substitution | `ISNULL(x, y)` / `COALESCE(x, y)` |
| Current timestamp | `SYSDATETIMEOFFSET()` (use over `GETDATE()` — keeps offset info) |
| String concat | `+` or `CONCAT()` |
| Auto-increment | `IDENTITY(1,1)` or `SEQUENCE` objects |
| Output changed rows | `OUTPUT` clause (like `RETURNING`) |
| Boolean columns | `BIT` (0/1, no true `BOOLEAN`) |

### Types

- Prefer `NVARCHAR` for user-facing text; since SQL Server 2019, UTF-8 collations let `VARCHAR` store Unicode too.
- Use `DATETIME2`/`DATETIMEOFFSET`, not legacy `DATETIME` (3.33 ms precision, 1753 lower bound).
- Money values: `DECIMAL(p,s)` — `FLOAT`/`REAL` are approximate and unsuitable.

### Bulk changes need batching

A single huge `DELETE`/`UPDATE` escalates to a full table lock. Delete/update in batches (`TOP (n)` loops with a delay between batches) to keep locks short and log growth controlled — same discipline as the zero-downtime migration rule.

### Index builds online

`WITH (ONLINE = ON)` lets reads/writes continue during index creation and rebuilds. Available in Standard Edition since SQL Server 2016 SP1 (Enterprise-only before that); long operations can be made resumable (`RESUMABLE = ON`) on newer versions. SQLite has no equivalent — its table rebuilds take a maintenance window (see above).

### Plan stability tooling

- **Query Store** records plan history and forces good plans back after regressions — enable it on production databases.
- Parameter sniffing symptoms (one plan serving wildly different parameter distributions) are addressed with `OPTION (RECOMPILE)` on the offending statement, not by disabling caching globally.

---

## Quick cross-engine cheat sheet

| Concern | PostgreSQL | MySQL 8.4 | SQLite | SQL Server 2022 |
|---|---|---|---|---|
| Upsert | `ON CONFLICT DO UPDATE` | `ON DUPLICATE KEY UPDATE` | `ON CONFLICT DO UPDATE` (3.24+) | `UPDATE`+`INSERT` / `MERGE`* |
| Returning rows | `RETURNING` | — (use `LAST_INSERT_ID()`) | `RETURNING` (3.35+) | `OUTPUT` |
| Limit rows | `LIMIT`/`FETCH FIRST` | `LIMIT` | `LIMIT` | `TOP` / `OFFSET…FETCH` |
| Covering index | `INCLUDE` | trailing key columns | plain columns | `INCLUDE` |
| Online index build | `CONCURRENTLY` | `ALGORITHM=INPLACE` | — (rebuild offline) | `ONLINE = ON` |
| Case-insensitive text | `CITEXT`/collation | collation (`utf8mb4_0900_ai_ci`) | `NOCASE`/`COLLATE` | collation (`_CI_`) |
| Exact money | `NUMERIC` | `DECIMAL` | integer minor units | `DECIMAL(p,s)` |

\* `MERGE` has documented concurrency caveats; back the merge target with a unique index and test under concurrent load.

## Sources

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite PRAGMA reference](https://www.sqlite.org/pragma.html)
- [SQLite ALTER TABLE (table-rebuild procedure)](https://www.sqlite.org/lang_altertable.html)
- [SQL Server Documentation](https://learn.microsoft.com/en-us/sql/sql-server/)
- [T-SQL ALTER TABLE](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-table-transact-sql)
- [SQL Server Index Guide](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes)
