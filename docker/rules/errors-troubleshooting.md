# Error Troubleshooting Rules

**Context:** Bu kural build, Compose, runtime veya network hatalarını teşhis ederken uygulanır. Hata sinyalini okumadan değişiklik yapmamak ve her hata alanı için sistematik bir kontrol sırası izlemek esas alınır.

## Prefer

- For build failures, inspect build context, COPY/ADD paths, `.dockerignore`, platform, ARG/ENV scope, and BuildKit mount syntax.
- For Compose failures, run `docker compose config` before `up`.
- For runtime failures, inspect logs, state, events, mounts, command, health checks, and resource limits.
- For networking failures, test DNS, target service listener, published ports, network membership, and subnet/firewall conflicts in that order.

## Avoid

- Do not treat `depends_on` as readiness; a service that times out waiting for `service_healthy` needs its dependency's healthcheck fixed first.
- Do not use host networking or privileged mode as a first fix.
- Do not change multiple Docker layers or Compose services at once when isolating an error.
- Do not cache container IPs when a connection fails after restart; use DNS names instead.

## Example

### Bad

```bash
# Changing everything at once to "fix" an unknown failure
docker compose down && docker system prune -a --volumes -f \
  && docker compose build --no-cache && docker compose up -d
```

### Good

```bash
# 1. Validate the file before running
docker compose config -q

# 2. Build failure: verify the path exists in the context and is not ignored
ls -la <context-directory>/src/app
cat .dockerignore
docker build --progress=plain . 2>&1 | head -20

# 3. Network failure, in order:
docker inspect --format='{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{end}}' <ctr1>
docker exec <ctr1> nslookup <ctr2-name>          # DNS resolves?
docker exec <target> ss -tlnp                    # Listening on 0.0.0.0?
docker compose port <service> <port>             # Host mapping correct?
```

## Verify

```bash
docker compose config
docker compose logs --tail=100
docker inspect <container>
docker network inspect <network>
```

Reference: references/errors-build.md, references/errors-build-diagnostics.md, references/errors-compose.md, references/errors-compose-diagnostics.md, references/errors-runtime-diagnostics.md, references/errors-networking-diagnostics.md
