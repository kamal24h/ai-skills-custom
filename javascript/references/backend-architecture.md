# Node.js Backend Architecture

Layering, dependency injection, middleware, errors, transactions, auth, caching, and shutdown for Express/Fastify services.

## When to Load

- Structuring a new Node.js service or reorganising an existing one
- Reviewing where business logic lives relative to route handlers
- Implementing authentication, validation, rate limiting, or caching
- Diagnosing lost writes, unhandled rejections, or requests dropped on deploy

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Layering & dependency injection | HIGH | `backend-` |
| 2 | Errors & error handling | HIGH | `backend-` |
| 3 | Data access & transactions | HIGH | `backend-` |
| 4 | Auth, validation, rate limiting | HIGH | `backend-` |
| 5 | Caching, logging, lifecycle | HIGH | `backend-` |

## Rule Index

- [`backend-layered-architecture`](../rules/backend-layered-architecture.md) — Route → service → repository
- [`backend-dependency-injection`](../rules/backend-dependency-injection.md) — Inject collaborators, do not import singletons
- [`backend-middleware-auth`](../rules/backend-middleware-auth.md) — Authentication as middleware, authorisation per action
- [`backend-input-validation`](../rules/backend-input-validation.md) — Schema-validate at the edge
- [`backend-rate-limiting`](../rules/backend-rate-limiting.md) — Per-identity limits with a shared store
- [`backend-custom-errors`](../rules/backend-custom-errors.md) — Typed application errors
- [`backend-error-handler`](../rules/backend-error-handler.md) — One terminal handler that maps errors to responses
- [`backend-database-transactions`](../rules/backend-database-transactions.md) — Atomic units of work
- [`backend-jwt-auth`](../rules/backend-jwt-auth.md) — Token issuing, verification, and refresh
- [`backend-redis-caching`](../rules/backend-redis-caching.md) — Cache keys, TTL, invalidation
- [`backend-api-response`](../rules/backend-api-response.md) — One response envelope across the API
- [`backend-graceful-shutdown`](../rules/backend-graceful-shutdown.md) — Drain before exit
- [`backend-structured-logging`](../rules/backend-structured-logging.md) — JSON logs with a correlation id

## Key Principles

### The layer boundary that matters

```
HTTP layer      routes/controllers   → parse, validate, map to/from HTTP. No business rules.
Service layer   services/use-cases   → business rules. Knows nothing about req/res.
Data layer      repositories         → persistence. Knows nothing about business rules.
```

The single most useful test: **could this service be called from a CLI script or a queue worker unchanged?** If it reads `req.query` or calls `res.status()`, it cannot, and the business rule is now locked inside HTTP.

```ts
// ❌ everything in the handler — untestable without an HTTP request
app.post('/orders', async (req, res) => {
  const items = req.body.items
  if (!items?.length) return res.status(400).json({ error: 'no items' })
  const total = items.reduce((s, i) => s + i.price * i.qty, 0)
  if (total > 100_000) return res.status(400).json({ error: 'too large' })
  const order = await db.query('INSERT INTO orders …')
  await mailer.send(req.user.email, 'Order placed')
  res.json(order)
})

// ✅ handler adapts HTTP; the service owns the rules
app.post('/orders', async (req, res, next) => {
  try {
    const input = createOrderSchema.parse(req.body)
    const order = await orderService.create(req.user.id, input)
    res.status(201).json({ data: order })
  } catch (err) { next(err) }
})
```

A "controller" that is three lines like this is not too thin — it is exactly the right size.

### Dependency injection without a framework

```ts
// composition root — the only place that constructs anything
export function buildContainer(config: Config) {
  const db = createPool(config.databaseUrl)
  const orderRepository = createOrderRepository(db)
  const orderService = createOrderService({ orderRepository, mailer, clock })
  return { orderService }
}
```

Constructor/factory injection keeps the dependency graph explicit and makes every unit testable with plain fakes. Importing a singleton (`import { db } from './db'`) inside a service creates a hidden edge that must be defeated with module mocking in every test — see [`test-di-mocking`](../rules/test-di-mocking.md).

Inject the clock and the id generator too. Time and randomness are dependencies; tests that cannot control them are flaky by construction.

### Validate at the edge, once

```ts
const createOrderSchema = z.object({
  items: z.array(z.object({ sku: z.string(), qty: z.number().int().positive() })).min(1),
  couponCode: z.string().optional(),
})
type CreateOrderInput = z.infer<typeof createOrderSchema>
```

Parse at the boundary and pass the typed result inward. Downstream code should never re-check shape — if it does, the boundary is not doing its job. Never trust `req.body` typed as an interface: that is an assertion about data you did not verify.

### Errors: typed at the source, mapped at the edge

```ts
export class AppError extends Error {
  constructor(message: string, readonly code: string, readonly status: number, readonly cause?: unknown) {
    super(message)
    this.name = new.target.name
  }
}
export class NotFound extends AppError {
  constructor(resource: string) { super(`${resource} not found`, 'NOT_FOUND', 404) }
}
```

```ts
// terminal handler — the only place that knows about HTTP status codes
app.use((err, req, res, _next) => {
  const isApp = err instanceof AppError
  if (!isApp) req.log.error({ err }, 'unhandled')
  res.status(isApp ? err.status : 500).json({
    error: { code: isApp ? err.code : 'INTERNAL', message: isApp ? err.message : 'Internal error' },
  })
})
```

Never leak `err.message` or a stack trace from an unknown error — they contain paths, queries, and library versions. In Express 4, async handlers must call `next(err)`; Express 5 forwards rejected promises automatically. Fastify handles async throws natively via `setErrorHandler`.

### Transactions are a service-layer concern

```ts
await db.transaction(async (tx) => {
  const order = await orderRepository.create(tx, input)
  await inventoryRepository.decrement(tx, input.items)
  return order
})
// side effects that cannot be rolled back happen AFTER commit
await outbox.publish('order.created', order.id)
```

Two failures to look for: repositories that open their own transactions (making composition impossible — pass the handle in), and non-transactional side effects such as emails or webhooks fired inside the transaction, which cannot be undone when it rolls back. Use an outbox or fire after commit.

### Caching

```ts
const key = `user:${id}:v2`
const hit = await redis.get(key)
if (hit) return JSON.parse(hit)
const user = await repository.findById(id)
await redis.set(key, JSON.stringify(user), 'EX', 300)
```

Include a version segment in the key so a shape change does not require flushing, set a TTL on everything (an entry with no expiry is a leak), and invalidate on write rather than hoping the TTL is short enough. For hot keys, guard against stampede: a single-flight lock or a jittered TTL prevents every request rebuilding the same value at the same second.

### Auth: authenticate once, authorise per action

Authentication middleware establishes *who*. Authorisation is a per-resource decision and belongs in the service, where the resource is loaded:

```ts
const order = await orderRepository.findById(id)
if (order.userId !== actor.id && !actor.isAdmin) throw new Forbidden()
```

Route-level role checks miss ownership entirely — the classic IDOR: a valid token for user A fetching user B's order.

JWT specifics: verify with an explicit `algorithms` allow-list (never accept `alg` from the token), keep access tokens short-lived with a rotating refresh token, and remember that a JWT cannot be revoked before expiry — for logout and ban you need a denylist or short expiry plus a session lookup.

### Structured logging and correlation

```ts
const logger = pino({ redact: ['req.headers.authorization', 'password', '*.token'] })
app.use((req, _res, next) => {
  req.id = req.get('x-request-id') ?? randomUUID()
  req.log = logger.child({ requestId: req.id })
  next()
})
```

JSON logs with a stable `requestId` are queryable; `console.log` strings are not. Redact credentials at the logger, not at each call site — the one that gets forgotten is the one that leaks.

### Graceful shutdown

```ts
async function shutdown(signal: string) {
  logger.info({ signal }, 'shutting down')
  server.close()                    // stop accepting new connections
  await worker?.close()             // let in-flight jobs finish
  await db.end()
  process.exit(0)
}
process.on('SIGTERM', () => void shutdown('SIGTERM'))
process.on('SIGINT',  () => void shutdown('SIGINT'))
```

Without this, every deploy drops in-flight requests and leaves half-finished work. Pair it with a readiness probe that starts failing before the drain begins, so the load balancer stops routing first. Add `process.on('unhandledRejection')` and `uncaughtException` handlers that log and exit — a process in an unknown state should be replaced, not continued.

## Sources

- [Node.js — Docs](https://nodejs.org/docs/latest/api/)
- [Express — Error handling](https://expressjs.com/en/guide/error-handling.html)
- [Fastify — Documentation](https://fastify.dev/docs/latest/)
- [OWASP — REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
- [OWASP — Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [Pino — Logger](https://getpino.io/)
- [The Twelve-Factor App](https://12factor.net/)
