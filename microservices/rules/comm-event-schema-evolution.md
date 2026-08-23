---
title: Evolve event schemas additively — published events are immutable contracts
impact: CRITICAL
tags: [communication, contracts, versioning]
---

# comm-event-schema-evolution

Once an event is published, consumers you cannot see may persist or replay it indefinitely. Renaming or repurposing a field breaks every consumer at once — often silently. Treat event payloads like public API contracts: evolve **additively**, never incompatibly.

## Bad — PHP

```php
// v2 of OrderPlaced renames total_cents -> amount_total and reuses status freely
class OrderPlaced {
    public function __construct(
        public string $orderId,
        public int $amountTotal,     // renamed: every consumer of
        public string $status,       // total_cents breaks on read
    ) {}
}

// Producer "upgrades" old events to the new shape when replaying history —
// consumers now receive two different meanings for one event type.
```

## Bad — TypeScript

```ts
interface OrderPlaced {
  orderId: string;
  amountTotal: number;   // was total_cents — breaking rename
  status: string;        // was enum 'paid'|'pending', now free-form
}

// Deleting optional fields consumers may still read:
const ev = { ...base, legacyFieldsRemoved: true };
```

## Good — PHP

```php
// Additive evolution: keep old fields, add new ones, narrow nothing.
#[Schema(version: 2)]
final class OrderPlacedV2 {
    public function __construct(
        public string $eventId,
        public string $orderId,
        public int $totalCents,          // unchanged — old consumers keep working
        public ?int $amountTotal = null, // new optional field for new consumers
        public string $schemaVersion = '2',
    ) {}
}

// Deprecation path: document the sunset date, ship both fields for a grace
// period, remove only after telemetry shows zero readers of the old field.
```

## Good — TypeScript

```ts
interface OrderPlacedV2 {
  event_id: string;
  order_id: string;
  total_cents: number;       // unchanged
  amount_total?: number;     // additive, optional
  schema_version: '2';
}

// Compatibility gate in CI: validate new payloads against the registry with
// BACKWARD compatibility mode before allowing publish.
import { SchemaRegistry } from '@kafkajs/confluent-schema-registry';
const registry = new SchemaRegistry({ host: process.env.SCHEMA_REGISTRY_URL! });
await registry.register({ type: SchemaType.AVRO, schema: rawAvro },
                        { compatibility: CompatibilityLevel.BACKWARD });
```

Rules of thumb: adding optional fields is safe; removing/renaming/retyping is not. Include `schema_version` (or embed it in envelope headers) so consumers can branch explicitly. Enforce compatibility mechanically — a schema registry (Confluent, Apicurio) with `BACKWARD` mode rejects breaking payloads at publish time instead of in production. Events are contracts first ([`comm-api-contracts`](comm-api-contracts.md)); their shape must not mirror internal DB columns.
