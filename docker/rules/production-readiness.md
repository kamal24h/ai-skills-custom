# Production Readiness Rules

**Context:** Bu kural bir image'i veya container'ı production'a taşımadan önce uygulanır. Runtime image boyutu, sağlık kontrolü, kaynak limitleri, sinyal yönetimi ve metadata kararlarını kapsar.

## Prefer

- Use minimal runtime images such as slim, alpine, distroless, or scratch when compatible.
- Add a health check that verifies actual readiness, with `--start-period` at least as long as expected startup.
- Configure restart policy, resource limits, and log rotation.
- Use OCI labels for image metadata (`org.opencontainers.image.*`).
- Pin base images by digest where reproducibility is required.
- End entrypoint scripts with `exec "$@"` so the application becomes PID 1 and receives signals.

## Avoid

- Do not ship SDKs, compilers, package caches, or test tooling in runtime images; keep them in build stages.
- Do not run production services without memory and CPU limits.
- Do not use shell-form entrypoints that swallow signals; the shell becomes PID 1 and never forwards SIGTERM.
- Do not write logs only inside the container filesystem.
- Do not declare `VOLUME` in application Dockerfiles; define named volumes at the orchestration layer instead.

## Example

### Bad

```dockerfile
# BAD: 850MB image with Go compiler, source code, test files
FROM golang:1.22
WORKDIR /app
COPY . .
RUN go build -o server
ENTRYPOINT ./server
```

Shell-form ENTRYPOINT makes `/bin/sh` PID 1; the app never receives SIGTERM and `docker stop` ends in a forced kill.

### Good

```dockerfile
# GOOD: 15MB image with only the binary
FROM golang:1.22 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o /server

FROM alpine:3.21
COPY --from=build /server /usr/bin/server
USER 65534:65534
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1
ENTRYPOINT ["/usr/bin/server"]
```

```yaml
services:
  app:
    image: myapp
    read_only: true
    tmpfs:
      - /tmp
    deploy:
      resources:
        limits:
          cpus: "2.0"
          memory: 512M
```

## Verify

```bash
docker inspect <container>
docker stats --no-stream
docker scout cves <image>
```

Reference: references/impl-production.md, references/impl-production-base-images.md, references/impl-production-examples.md, references/impl-production-anti-patterns.md
