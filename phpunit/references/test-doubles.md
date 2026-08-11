# Test Doubles

Stubs, mocks, fakes, and the design signals that appear when doubling becomes difficult.

## When to Load

- Deciding whether a collaborator needs a stub, a mock, or a fake
- A test breaks on every refactor even though behaviour did not change
- The class under test cannot be constructed without infrastructure
- Doubling something final, static, or constructed with `new` inside a method

## Rule Index

- [`double-stub-vs-mock`](../rules/double-stub-vs-mock.md) — Stub for state, mock for interaction
- [`double-no-mock-sut`](../rules/double-no-mock-sut.md) — Never double the class under test
- [`double-interface-not-concrete`](../rules/double-interface-not-concrete.md) — Double contracts you own
- [`double-fake-over-chain`](../rules/double-fake-over-chain.md) — Hand-written fakes for stateful collaborators

## The Five Kinds

| Kind | Purpose | PHPUnit |
|---|---|---|
| **Dummy** | Fills a parameter, never used | `createStub()` |
| **Stub** | Returns canned values | `createStub()`, `createConfiguredStub()` |
| **Spy** | Records calls, asserted afterwards | `createMock()` without `expects()`, or a fake |
| **Mock** | Asserts calls as they happen | `createMock()` + `expects()` |
| **Fake** | Working lightweight implementation | Hand-written class |

The distinction that matters day to day: a **stub is an input** to the system under test, a **mock is an assertion about its output**. Getting this backwards — asserting on every input call — is what produces brittle suites.

## API Reference (PHPUnit 12)

```php
// Stubs — no expectations possible
$stub = $this->createStub(TaxRateProvider::class);
$stub->method('forCountry')->willReturn(0.19);
$stub = $this->createConfiguredStub(TaxRateProvider::class, ['forCountry' => 0.19]);

// Mocks — expectations available
$mock = $this->createMock(Mailer::class);
$mock->expects($this->once())->method('send')->with('a@b.co');
$mock = $this->createConfiguredMock(Mailer::class, ['send' => true]);

// Several interfaces at once
$double = $this->createMockForIntersectionOfInterfaces([Countable::class, Traversable::class]);
```

### Return configuration

```php
->willReturn($value)
->willReturnOnConsecutiveCalls($a, $b, $c)     // order-dependent — prefer a fake
->willReturnCallback(fn(string $c) => $rates[$c] ?? 0.0)
->willReturnSelf()                              // fluent interfaces
->willReturnArgument(0)                         // pass-through
->willThrowException(new ConnectionLost())
```

### Argument matching

```php
->with('a@b.co', $this->isInstanceOf(Receipt::class))
->with($this->callback(fn(Receipt $r) => $r->orderId() === 'o_1'))
->with($this->anything(), $this->greaterThan(0))
```

`$this->callback()` is the flexible option and gives better failure output than reproducing a complex object for `equalTo()`.

### Invocation counts

```php
->expects($this->once())        // exactly one call
->expects($this->never())       // useful: "no email is sent when validation fails"
->expects($this->exactly(2))
->expects($this->atLeastOnce())
->expects($this->any())         // the default — no assertion
```

`$this->never()` is the most under-used and most valuable: it asserts an absence, which is otherwise untestable.

## Choosing

```
Is the collaborator's call the observable behaviour?
├── Yes → mock with expects()          e.g. an email is sent, an event is published
└── No
    ├── Does it hold state the test asserts on later?
    │   ├── Yes → hand-written fake     e.g. repository, cache, queue
    │   └── No  → stub                  e.g. a rate provider, a config source
    └── Is it noise (logger, metrics)?  → null implementation
```

## When Doubling Gets Hard, Change the Design

| Symptom | Underlying problem | Fix |
|---|---|---|
| Need `createPartialMock` on the SUT | The class has a hidden collaborator | Extract and inject it |
| Cannot double — the class is `final` | Depending on a concrete type | Introduce an interface you own |
| `new Foo()` inside the method | Construction coupled to logic | Inject a factory or the instance |
| A static call to a service | Global dependency | Inject an instance |
| Six doubles for one test | The SUT has too many responsibilities | Split the class |
| Test asserts a call sequence | Testing implementation, not behaviour | Assert on the outcome |

Installing an extension to double a final class (`dg/bypass-finals`, `uopz`) treats the symptom. The interface is the fix, and it is usually three lines.

## Fakes Worth Writing

```php
final class SpyMailer implements Mailer
{
    /** @var list<array{string, string}> */
    private array $sent = [];

    public function send(string $to, string $template): void
    {
        $this->sent[] = [$to, $template];
    }

    /** @return list<string> */
    public function templatesSentTo(string $to): array
    {
        return array_values(array_map(
            fn(array $s) => $s[1],
            array_filter($this->sent, fn(array $s) => $s[0] === $to),
        ));
    }
}
```

```php
$this->assertSame(['welcome'], $mailer->templatesSentTo('a@b.co'));
```

Reads as a statement about outcomes rather than about invocations, and it does not break when the service starts batching sends.

**Contract-test your fakes.** Write one abstract test case against the interface and run it against both the real implementation and the fake — otherwise the fake drifts and the suite passes against a fiction:

```php
abstract class OrderRepositoryContractTest extends TestCase
{
    abstract protected function repository(): OrderRepository;

    public function test_it_returns_null_for_an_unknown_id(): void
    {
        $this->assertNull($this->repository()->find('nope'));
    }
}
```

## Alternatives

- **Mockery** — expressive fluent API, better partial-double ergonomics; needs `mockery/mockery` plus the PHPUnit integration to assert expectations at teardown.
- **Prophecy** — no longer bundled with PHPUnit; usable via `phpspec/prophecy-phpunit`.
- **Anonymous classes** — for a one-off double of a small interface, `new class implements Clock { … }` is often the shortest readable option and needs no framework at all.

## Sources

- [PHPUnit — Test doubles](https://docs.phpunit.de/en/12.0/test-doubles.html)
- [Martin Fowler — Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
- [Martin Fowler — Test Double](https://martinfowler.com/bliki/TestDouble.html)
- [Mockery documentation](http://docs.mockery.io/en/latest/)
