# Dockerfile Basics Rules

**Context:** Bu kural Dockerfile yazarken veya düzenlerken uygulanır. Temel instruction seçimi (FROM, COPY, WORKDIR, USER, ENTRYPOINT/CMD), base image sabitleme ve katman hijyeni kararlarını kapsar.

## Prefer

- Start BuildKit Dockerfiles with `# syntax=docker/dockerfile:1`.
- Use `COPY` for local files and reserve `ADD` for archive extraction or remote sources with a reason.
- Use `WORKDIR` instead of `RUN cd`.
- Use exec form for `ENTRYPOINT` and `CMD`; shell form makes `sh` PID 1 and the app never receives signals.
- Create and switch to a non-root `USER` in the final runtime stage.
- Pin base image tags explicitly; an omitted tag defaults to `latest`.

## Avoid

- Do not use `latest` for production base images.
- Do not place secrets in `ARG`, `ENV`, or copied files; ARG appears in `docker history`, ENV persists via `docker inspect`.
- Do not split `apt-get update` and `apt-get install` across layers; the cached index goes stale and installs fail.
- Do not leave package manager caches in runtime layers; cleanup must happen in the same RUN or the bytes remain.

## Example

### Bad

```dockerfile
# BAD -- non-deterministic, root user, stale apt cache risk
FROM node:latest
COPY . /app
RUN apt-get update
RUN apt-get install -y curl
ENV API_KEY=sk-1234567890
ENTRYPOINT /usr/bin/myapp
```

Shell-form ENTRYPOINT wraps the command in `/bin/sh -c`, so `sh` is PID 1 and `docker stop` ends in a 10-second timeout plus SIGKILL.

### Good

```dockerfile
# syntax=docker/dockerfile:1
FROM node:20.11-bookworm-slim AS runtime

RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY --chown=appuser:appuser . .
USER appuser

ENTRYPOINT ["/usr/bin/myapp"]
```

## Verify

```bash
docker build .
docker history <image>
```

Reference: references/syntax-dockerfile.md, references/syntax-dockerfile-instructions.md, references/syntax-dockerfile-anti-patterns.md, references/syntax-dockerfile-examples.md
