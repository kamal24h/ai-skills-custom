---
title: Publish domain events via a transactional outbox — never commit DB + broker separately
impact: CRITICAL
tags: [data, consistency, messaging]
---

# data-transactional-outbox

A service that writes to its database **and** publishes an event as two separate operations has a distributed-consistency bug: crash between them means either a state change nobody heard about, or an event about a change that never happened. Two-phase commit across the DB and the broker is not the answer (see [`boundary-database-per-service`](boundary-database-per-service.md) rationale) — the outbox is.

## Bad — PHP

```php
public function placeOrder(Order $order): void {
    DB::transaction(function () use ($order) {
        $order->save();                       // committed...
    });
    $this->kafka->publish('orders', new OrderPlaced($order->id));  // ...or this never runs
}
```

## Bad — TypeScript

```ts
async function placeOrder(order: Order) {
  await db.transaction(async (tx) => { await tx.insert(orders).values(order); });
  await producer.send({ topic: 'orders', messages: [{ value: JSON.stringify(new OrderPlaced(order.id)) }] });
  // if send fails after commit: lost event; if before: phantom event
}
```

## Good — PHP

```php
public function placeOrder(Order $order): void {
    DB::transaction(function () use ($order) {
        $order->save();
        // Same transaction: the event row commits atomically with the state change
        DB::table('outbox')->insert([
            'event_id'   => (string) Str::uuid(),
            'type'       => 'OrderPlaced',
            'payload'    => json_encode(['order_id' => $order->id]),
            'created_at' => now(),
        ]);
    });
}

// A relay (scheduled job / Debezium CDC) publishes pending rows and marks them sent.
// Consumers still dedupe by event_id ([comm-idempotent-consumers](comm-idempotent-consumers.md)).
```

## Good — TypeScript

```ts
async function placeOrder(order: Order) {
  const eventId = crypto.randomUUID();
  await db.transaction(async (tx) => {
    await tx.insert(orders).values(order);
    await tx.insert(outbox).values({ eventId, type: 'OrderPlaced', payload: JSON.stringify({ order_id: order.id }) });
  }); // atomic
}

// Relay polls: SELECT ... WHERE published_at IS NULL ORDER BY id FOR UPDATE SKIP LOCKED LIMIT 100
// then publish, then UPDATE outbox SET published_at = now().
```

Key properties: insert into `outbox` in the **same transaction** as the state change; a separate relay (polling publisher or CDC such as Debezium) delivers rows to the broker at-least-once; consumers stay idempotent. Give the outbox table an index on `(published_at, id)`, purge delivered rows on a schedule, and keep payloads in the public schema versioned per [`comm-event-schema-evolution`](comm-event-schema-evolution.md).

Pattern reference: [microservices.io — Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html).
