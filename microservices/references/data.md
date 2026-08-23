# Data Management

**Impact:** CRITICAL · **Prefix:** `data-` · **4 rules**

No distributed two-phase commit. Each service owns its data; cross-service consistency is eventual, coordinated via sagas, events, and — where reads need different shapes — CQRS.

## Load When

- Implementing a workflow that spans 2+ services (order + payment + inventory)
- Deciding between orchestrated and choreographed saga
- Considering event sourcing as the source of truth
- Separating read and write models (CQRS)
- Debugging dual-write bugs ("we charged the card but didn't save the order")

## Rules

| Rule | Summary |
|------|---------|
| [`data-saga-orchestration`](../rules/data-saga-orchestration.md) | Central orchestrator drives steps + compensations |
| [`data-saga-choreography`](../rules/data-saga-choreography.md) | Services react to events — no central coordinator |
| [`data-event-sourcing`](../rules/data-event-sourcing.md) | Events are the source of truth; state is a projection |
| [`data-cqrs`](../rules/data-cqrs.md) | Separate write model from read projections |
| [`data-transactional-outbox`](../rules/data-transactional-outbox.md) | Publish events atomically with the state change that caused them |

## Orchestration vs Choreography

| | Orchestration | Choreography |
|--|--|--|
| Flow visible in one place | ✓ (orchestrator) | ✗ (spread across services) |
| New step = touch | orchestrator + 1 service | 1 service |
| Single point of failure | orchestrator | — |
| Best for | complex, evolving workflows | simple, stable flows |

**Rule of thumb:** start with choreography for 2–3 steps; graduate to orchestration when the flow has 4+ steps or branching.

## Outbox Pattern (avoids dual-write)

Problem: writing to DB **and** publishing to broker is not atomic. Crash between them → inconsistent state.

Solution: single DB transaction writes both domain row and an `outbox` row. A relay polls `outbox` and publishes, marking rows as sent.

```sql
CREATE TABLE outbox (
  id           BIGSERIAL PRIMARY KEY,
  aggregate_id VARCHAR(64) NOT NULL,
  event_type   VARCHAR(64) NOT NULL,
  payload      JSONB       NOT NULL,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
  published_at TIMESTAMPTZ
);
CREATE INDEX outbox_unpublished ON outbox (created_at) WHERE published_at IS NULL;
```

## Saga Skeleton

```
step_1 ──success──► step_2 ──success──► step_3 ──success──► DONE
   │                   │                   │
   │ failure           │ failure           │ failure
   ▼                   ▼                   ▼
                    compensate_1
                    compensate_1 + 2
                    compensate_1 + 2 + 3
```

Compensations must be **idempotent** (may be retried) and **semantic** (refund, not delete; cancellation email, not "unsend").

## Event Sourcing — When to Use

- ✓ Audit is a hard requirement (finance, healthcare, legal)
- ✓ Replay / time-travel is a product feature
- ✓ Multiple read models derive from the same write events
- ✗ Team has never done it before — high operational complexity
- ✗ Domain is CRUD-shaped; events are just "row changed"

## CQRS — When to Use

- ✓ Read and write shapes diverge significantly (denormalised search vs normalised write)
- ✓ Read scale ≫ write scale; different storage (e.g., Postgres write → Elasticsearch read)
- ✓ Paired with event sourcing
- ✗ Simple domain where one model serves both reads and writes cleanly

## Eventual Consistency UX

- Immediate UI feedback via optimistic update ("Order placed") + reconcile on event
- Polling endpoint (`GET /orders/123`) shows current projected state
- WebSocket / SSE pushes state transitions to the client
- Always expose `updated_at` or `version` so clients can detect drift

## Sources

- [Microservices.io — Saga](https://microservices.io/patterns/data/saga.html)
- [Martin Fowler — Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html)
- [Microservices.io — Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html)
- [Martin Fowler — CQRS](https://martinfowler.com/bliki/CQRS.html)
