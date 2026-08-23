# BuildKit Mount Rules

**Context:** Bu kural Dockerfile içinde BuildKit mount tiplerini (`cache`, `secret`, `ssh`, `bind`, `tmpfs`) kullanırken uygulanır. Paket yöneticisi cache'leri, build-time kimlik bilgileri ve özel depolara erişim gerektiren build adımlarında devreye girer.

## Prefer

- Use `RUN --mount=type=cache` for package manager caches.
- Use `RUN --mount=type=secret` for build-time credentials.
- Use `RUN --mount=type=ssh` for private repository access.
- Keep secret and SSH mounts scoped to the single `RUN` instruction that needs them.
- Use `sharing=locked` for apt cache mounts; apt uses internal lock files.
- Add known hosts with `ssh-keyscan` before SSH operations so the non-interactive build does not hang.

## Avoid

- Do not pass secrets with `ARG` or `ENV`; ARG appears in `docker history`, ENV persists in image metadata.
- Do not expect cache mounts to become part of the image; copy artifacts out of cache-mounted directories within the same `RUN`.
- Do not rely on BuildKit-only syntax without a syntax directive; it must be the very first line, before any comment or blank line.
- Do not add `rm -rf /var/lib/apt/lists/*` when the apt lists directory is a cache mount; cleaning defeats the persistent cache.

## Example

### Bad

```dockerfile
# Secret visible in docker history and image metadata
ARG DATABASE_PASSWORD=secret123
ENV API_KEY=sk-1234567890
RUN curl -H "Authorization: Bearer $API_KEY" https://api.example.com

# Binary written into cache-mounted target/ -- it disappears after RUN
RUN --mount=type=cache,target=/app/target/ \
    cargo build --release
```

### Good

```dockerfile
# syntax=docker/dockerfile:1

FROM rust:1.77 AS build
WORKDIR /app

COPY Cargo.toml Cargo.lock ./
COPY src/ src/

RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm ci --prefer-offline

RUN --mount=type=cache,target=/app/target/ \
    --mount=type=cache,target=/usr/local/cargo/git/db \
    --mount=type=cache,target=/usr/local/cargo/registry/ \
    cargo build --release \
    && cp target/release/myapp /usr/local/bin/myapp
```

```bash
# Secrets are provided at build time, never stored in layers:
docker build --secret id=npmrc,src=$HOME/.npmrc .

# SSH agent forwarding -- the private key never enters the image:
eval $(ssh-agent)
ssh-add ~/.ssh/id_ed25519
docker build --ssh default .
```

## Verify

```bash
DOCKER_BUILDKIT=1 docker build --progress=plain .
docker builder prune --filter type=exec.cachemount
```

Reference: references/syntax-buildkit-mounts.md, references/syntax-buildkit-examples.md, references/syntax-buildkit-anti-patterns.md
