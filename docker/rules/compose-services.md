# Compose Services Rules

**Context:** Bu kural `compose.yaml` içinde servis tanımlarken uygulanır. Servis başlatma sırası, sağlık kontrolü, port yayınlama, kalıcılık ve gizli bilgi yönetimi kararlarında devreye girer.

## Prefer

- Use `compose.yaml` and omit the deprecated `version:` field.
- Define health checks for databases, caches, and long-running services.
- Use `depends_on` with `condition: service_healthy` when startup order requires readiness.
- Use named volumes for persistence and declare them at the top level.
- Bind development ports to `127.0.0.1` unless network-wide exposure is required.
- Use profiles for optional debug/admin services.
- Set explicit resource limits with `deploy.resources` so a single container cannot exhaust the host.
- Interpolate required values as `${VAR:?message}` instead of hardcoding them.

## Avoid

- Do not use `container_name` for services that may need scaling; a fixed name makes `--scale` fail with a name conflict.
- Do not hardcode secrets in `environment`; they appear in `docker inspect`, process listings, and logs.
- Do not expose internal-only services with `ports`.
- Do not rely on bare `depends_on` as a readiness check; short form waits only for container start, not application readiness.
- Do not use anonymous volumes for persistent data; `docker compose down` removes them.

## Example

### Bad

```yaml
# WRONG -- app starts before the database accepts connections
services:
  app:
    depends_on:
      - db
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: "super-secret-password"
```

### Good

```yaml
services:
  app:
    build:
      context: .
      target: production
    ports:
      - "127.0.0.1:3000:3000"
    depends_on:
      db:
        condition: service_healthy
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
    restart: unless-stopped
  db:
    image: postgres:16-alpine
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD:?Database password required}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

volumes:
  db-data:
```

## Verify

```bash
docker compose config
docker compose ps
```

Reference: references/syntax-compose-services.md, references/syntax-compose-services-attributes.md, references/syntax-compose-services-examples.md, references/syntax-compose-services-anti-patterns.md
