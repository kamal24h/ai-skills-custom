# Protocol Alternatives — GraphQL & gRPC

REST covers most public APIs. This guide documents when **GraphQL** and **gRPC** are the better contract style, and their core design rules, compiled from the official protocol documentation.

## 1. Choosing the Contract Style

| Concern | REST | GraphQL | gRPC |
|---|---|---|---|
| Best fit | Public/resource-oriented APIs | Aggregated, client-specific views | Internal service-to-service RPC |
| Contract | OpenAPI (descriptive) | SDL schema (normative) | `.proto` files (normative) + codegen |
| Transport | HTTP/1.1+ verbs | HTTP POST, single endpoint | HTTP/2 multiplexed streams |
| Payload shape | Server-defined | Client-defined (exact fields) | Binary protobuf messages |
| Over/under-fetch | Common problem | Solved by field selection | Rare (fixed messages) |
| Streaming | Limited (SSE/WebSocket) | Subscriptions | Native unary/server/client/bidi streaming |
| Browser support | Native | Native JSON | Requires gRPC-Web/proxy layer |
| Caching | HTTP caching semantics | Application-level | Application-level |
| Error model | Status codes + envelope | Partial `data` + `errors` array | Rich status codes + deadline propagation |

## 2. GraphQL Design Rules (graphql.org)

### Schema first, evolution over versioning

```graphql
type Query {
  user(id: ID!): User
}

type User {
  id: ID!
  email: String!            # adding fields is non-breaking
  name(full: Boolean): String
  legacyField: String @deprecated(reason: "Use `name`. Removed 2027-01.")
}
```

- Adding **nullable fields** and **new types** is non-breaking; removing or retyping fields is breaking — deprecate with `@deprecated` and a removal date instead of shipping `/v2`.
- Expose a schema registry/check-in CI: validate that proposed changes are backward-compatible before merge.

### Resolvers and the N+1 trap

Each field resolves independently; naive resolvers issue one query per node. Batch within a request using DataLoader-style memoized caches so N sibling lookups collapse into one batched query.

### Errors and partial results

```json
{
  "data": { "user": { "name": "Ada" } },
  "errors": [
    { "message": "Email not authorized", "path": ["user", "email"],
      "extensions": { "code": "FORBIDDEN" } }
  ]
}
```

- Non-null field failures null out up to the nearest nullable ancestor — design nullability deliberately.
- Use stable machine codes in `extensions.code` (`UNAUTHENTICATED`, `BAD_USER_INPUT`, …); mirror your REST error-code taxonomy where possible.

### Security checklist

- Enforce **depth limiting** and **query cost/complexity analysis**; clients can otherwise ask arbitrarily expensive queries.
- Prefer **persisted queries** for first-party clients.
- Disable or gate **introspection** and the graphiql IDE in production unless you intentionally run a public API.

## 3. gRPC Design Rules (grpc.io)

### Contract and codegen

```protobuf
syntax = "proto3";

package orders.v1;

service OrderService {
  rpc GetOrder(GetOrderRequest) returns (OrderResponse);
  rpc WatchOrders(GetOrderRequest) returns (stream OrderEvent); // server streaming
}

message GetOrderRequest {
  string order_id = 1;
}
```

- Field numbers are wire contracts — never reuse or renumber them on deployed messages; reserve removed numbers with `reserved`.
- Treat package names as API namespaces (`orders.v1`) — breaking changes get a new package, mirroring URL-versioned REST.

### Streaming and deadlines

- Pick the smallest streaming mode that fits: unary → server-stream → client-stream → bidi.
- Always propagate **deadlines**; every hop inherits the caller's deadline by default and must cancel work when it expires.
- Model failures with canonical status codes (`NOT_FOUND`, `FAILED_PRECONDITION`, `UNAVAILABLE`, …) and structured error details — not string messages alone.

### Operational essentials

- Terminate TLS at the edge or use mTLS mesh-sidecars; plaintext h2c only inside trusted networks.
- Add the standard **health checking protocol** (`grpc.health.v1`) for probes.
- Auth/metadata via interceptors, not per-method boilerplate.

## 4. Mixing Protocols

A common production topology: **gRPC between services**, **REST (or GraphQL) at the edge** for browsers/mobile, translated by a gateway (grpc-gateway style). Keep one domain model behind both facades — do not fork business validation per protocol.

## Related Rules

- Error taxonomy consistency: [`error-error-codes`](../rules/error-error-codes.md), [`error-consistent-format`](../rules/error-consistent-format.md)
- Versioning/deprecation policy applies equally to GraphQL fields and proto packages: [`ver-deprecation`](../rules/ver-deprecation.md)

## Sources

- [GraphQL Official Documentation — Learn](https://graphql.org/learn/)
- [GraphQL Specification](https://spec.graphql.org/)
- [GraphQL Best Practices — Versioning](https://graphql.org/learn/best-practices/#versioning)
- [gRPC Official Documentation](https://grpc.io/docs/)
- [Protocol Buffers Overview & Style Guide](https://protobuf.dev/programming-guides/style/)
- [gRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md)
