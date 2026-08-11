---
title: Prefer a Hand-Written Fake Over a Long willReturn Chain
impact: MEDIUM
impactDescription: Doubles configured with many willReturnOnConsecutiveCalls become order-dependent puzzles that break on any refactor
tags: phpunit, test-doubles, fakes, readability, maintenance
---

## Prefer a Hand-Written Fake Over a Long willReturn Chain

**Impact: MEDIUM — Once a double needs stateful behaviour, a fake is shorter to read, reusable, and immune to call-order changes**

Generated doubles answer questions. When the collaborator has *state* — a repository, a cache, a queue — a small in-memory implementation is the better tool.

## Bad Example

```php
public function test_it_moves_the_order_through_fulfilment(): void
{
    $repository = $this->createMock(OrderRepository::class);
    $repository->method('find')
        ->willReturnOnConsecutiveCalls(          // ❌ depends on exact call order
            $this->anOrder(status: Status::Paid),
            $this->anOrder(status: Status::Picked),
            $this->anOrder(status: Status::Packed),
        );
    $repository->expects($this->exactly(3))->method('save');

    $this->service->fulfil('o_1');

    // …and there is no way to assert on the final persisted state,
    //    because nothing was ever actually stored
}
```

Adding one extra `find()` call anywhere in the implementation shifts every subsequent answer, and the test fails with a type error far from the cause. The final state cannot be asserted at all.

## Good Example

```php
final class InMemoryOrderRepository implements OrderRepository
{
    /** @var array<string, Order> */
    private array $orders = [];

    public function __construct(Order ...$orders)
    {
        foreach ($orders as $order) { $this->orders[$order->id()] = $order; }
    }

    public function find(string $id): ?Order { return $this->orders[$id] ?? null; }

    public function save(Order $order): void { $this->orders[$order->id()] = $order; }
}
```

```php
public function test_it_moves_the_order_through_fulfilment(): void
{
    $repository = new InMemoryOrderRepository($this->anOrder(id: 'o_1', status: Status::Paid));

    (new FulfilmentService($repository))->fulfil('o_1');

    $this->assertSame(Status::Shipped, $repository->find('o_1')->status());
}
```

The test now states an outcome instead of a call sequence, and it does not care how many times the service reads or writes.

## Notes

- Fakes pay off when reused. One `InMemoryOrderRepository` in `Tests\Support` serves the whole suite; a `willReturn` chain serves one test.
- Keep fakes **simple**. A fake with its own branching logic is code that needs tests. If it grows conditionals, the interface is probably too wide.
- Add assertion helpers to fakes where useful: `$mailer->sentTo('a@b.co')`, `$queue->pending()`. This keeps interaction checks readable without mock expectations.
- **Contract-test the fake.** Write one abstract test case for the interface and run it against both the real implementation and the fake — otherwise the fake drifts and the suite passes against a fiction.
- `createConfiguredMock(Interface::class, ['find' => $order])` is a good middle ground for the simple stateless case.

## Why

- **Order independence**: The test survives implementation changes that alter how often collaborators are called.
- **Assertable end state**: You can verify what was stored, not just that `save()` was invoked.
- **Reuse**: One well-made fake removes double setup from dozens of tests.
