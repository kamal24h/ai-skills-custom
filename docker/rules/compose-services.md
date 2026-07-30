# Compose Services Rules

## Prefer

- Use `compose.yaml` and omit the deprecated `version:` field.
- Define health checks for databases, caches, and long-running services.
- Use `depends_on` with `condition: service_healthy` when startup order requires readiness.
- Use named volumes for persistence and declare them at the top level.
- Bind development ports to `127.0.0.1` unless network-wide exposure is required.
- Use profiles for optional debug/admin services.

## Avoid

- Do not use `container_name` for services that may need scaling.
- Do not hardcode secrets in `environment`.
- Do not expose internal-only services with `ports`.
- Do not rely on bare `depends_on` as a readiness check.

## Verify

```bash
docker compose config
docker compose ps
```
