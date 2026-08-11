# Testing AI and Probabilistic Code

Verifying behaviour that is not deterministic, and keeping the deterministic parts deterministic.

## When to Load

- Testing a feature backed by an LLM or any probabilistic model
- Deciding what can be asserted exactly and what needs a tolerance
- A test suite calls a live model API and is slow, expensive, or flaky
- Using an AI assistant to generate tests

## First: Separate What Is Actually Non-Deterministic

Most of an "AI feature" is ordinary deterministic code and should be tested as such:

```
Deterministic — test normally      │ Non-deterministic — needs the techniques below
───────────────────────────────────┼──────────────────────────────────────────────
Prompt construction                │ The model's response content
Request payload and headers        │ Semantic quality of the output
Response parsing and validation    │ Whether a judgement is "correct"
Retry, timeout, backoff logic      │
Token counting and truncation      │
Error mapping and fallbacks        │
Cost accounting                    │
```

The largest win is putting the model behind an interface you own, so the entire deterministic layer is testable with a stub:

```php
interface CompletionClient
{
    public function complete(Prompt $prompt): Completion;
}
```

```php
public function test_it_includes_the_customer_history_in_the_prompt(): void
{
    $client = new RecordingCompletionClient(Completion::of('ok'));

    (new SupportAgent($client))->reply($this->aTicket(history: ['prior issue']));

    $this->assertStringContainsString('prior issue', $client->lastPrompt()->text());
}
```

No model call, no cost, no flakiness — and prompt regressions are a common real defect.

## Techniques for the Non-Deterministic Part

### 1. Assert on invariants, not on text

```php
// ❌ will break on any model update or temperature change
$this->assertSame('The order total is €45.00.', $response->text());

// ✅ properties that must hold regardless of phrasing
$this->assertStringContainsString('45.00', $response->text());
$this->assertLessThanOrEqual(280, mb_strlen($response->text()));
$this->assertStringNotContainsString('sk-', $response->text());     // no leaked secrets
$this->assertSame('summary', $response->type());
```

### 2. Constrain the output format

Structured output (JSON mode, tool calls, or a schema) turns "did it answer well" into "does it parse and validate":

```php
$parsed = json_decode($response->text(), true, flags: JSON_THROW_ON_ERROR);
$this->assertSame(['sentiment', 'confidence'], array_keys($parsed));
$this->assertContains($parsed['sentiment'], ['positive', 'neutral', 'negative']);
$this->assertGreaterThanOrEqual(0.0, $parsed['confidence']);
```

Schema validation catches the majority of real failures and is fully deterministic on your side.

### 3. Statistical thresholds, run outside the unit suite

```php
#[Group('llm-eval')]
public function test_it_classifies_sentiment_correctly_at_least_80_percent_of_the_time(): void
{
    $correct = 0;
    foreach (self::labelledSamples() as [$text, $expected]) {
        if ($this->classifier->classify($text) === $expected) { $correct++; }
    }

    $this->assertGreaterThanOrEqual(0.8, $correct / count(self::labelledSamples()));
}
```

Put these behind `#[Group('llm-eval')]` and exclude them from the default run — they are slow, cost money, and their failure means "quality regressed", which is a different signal from "the code is broken".

### 4. LLM-as-judge, for criteria that cannot be expressed as a rule

Ask a model to score the output against explicit criteria, and require structured output so the score is parseable. Treat it as a **quality metric with error bars**, never as a unit-test assertion: judges are themselves non-deterministic and biased toward verbosity and their own phrasing style. Pin the judge model version, and validate the judge against human labels before trusting it.

### 5. Negative testing

The most valuable AI tests assert what must **never** happen:

```php
#[DataProvider('promptInjectionAttempts')]
public function test_it_does_not_reveal_the_system_prompt(string $attack): void
{
    $response = $this->agent->reply($attack);

    $this->assertStringNotContainsString('You are a helpful', $response->text());
}
```

Cover: system-prompt disclosure, prompt injection via user content, out-of-scope advice (financial, medical, legal), PII echoing, and secret leakage. These are safety requirements, so run them in CI even though they are slow.

### 6. Record and replay

Record real responses once, replay them in CI:

```php
$client = new ReplayingCompletionClient(__DIR__ . '/fixtures/completions');
```

Gives deterministic, free, fast tests over realistic data. The trade-off is drift — recordings do not reflect the current model — so re-record on a schedule and keep a small live-eval suite as the canary.

## Suite Organisation

```
tests/Unit/Ai/           → prompt building, parsing, retries. Stubs only. Runs always.
tests/Integration/Ai/    → replayed fixtures. Runs always.
tests/Eval/              → live model, statistical thresholds. #[Group('llm-eval')], nightly.
```

```bash
vendor/bin/phpunit --exclude-group llm-eval        # default
vendor/bin/phpunit --group llm-eval                # nightly / pre-release
```

Never let a live model call into the default suite. It makes CI cost money, fail on network problems, and vary by time of day.

## Determinism Settings

Set `temperature: 0` (or the provider's equivalent) and pin the model version in tests. This reduces variance substantially but does not eliminate it — batching, hardware, and provider-side changes still produce different outputs for identical inputs. Design assertions that tolerate that; do not assume `temperature: 0` gives you exact reproducibility.

## Using AI to Write Tests

Generated tests are a scaffold, not a deliverable:

1. **List scenarios before generating code** — boundaries, error paths, invariants. A model asked for "tests for this class" produces happy-path tests that mirror the implementation, including its bugs.
2. **Provide an existing high-quality test as an example** so the output matches project conventions.
3. **Verify each test fails when it should.** Break the implementation deliberately and confirm the test catches it. A generated test that passes against broken code is worse than none.
4. **Reject tests that mirror the implementation.** If the generated assertion recomputes the expected value with the production formula, replace it with a hard-coded value.
5. **Review coverage of error paths** — this is what generated suites most consistently miss.

## Sources

- [PHPUnit — Documentation](https://docs.phpunit.de/en/12.0/)
- [Anthropic — Create strong empirical evaluations](https://docs.claude.com/en/docs/test-and-evaluate/develop-tests)
- [Anthropic — Increase output consistency](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/increase-consistency)
- [OWASP — Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
