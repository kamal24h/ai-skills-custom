# Error Troubleshooting Rules

## Prefer

- For build failures, inspect build context, COPY/ADD paths, `.dockerignore`, platform, ARG/ENV scope, and BuildKit mount syntax.
- For Compose failures, run `docker compose config` before `up`.
- For runtime failures, inspect logs, state, events, mounts, command, health checks, and resource limits.
- For networking failures, test DNS, target service listener, published ports, network membership, and subnet/firewall conflicts in that order.

## Avoid

- Do not treat `depends_on` as readiness.
- Do not use host networking or privileged mode as a first fix.
- Do not change multiple Docker layers or Compose services at once when isolating an error.

## Verify

```bash
docker compose config
docker compose logs --tail=100
docker inspect <container>
docker network inspect <network>
```
