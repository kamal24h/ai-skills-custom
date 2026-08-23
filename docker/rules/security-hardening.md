# Security Hardening Rules

**Context:** Bu kural image build ve container runtime güvenliğini sıkılaştırırken uygulanır. Kullanıcı ayrıcalıkları, capability'ler, dosya sistemi izinleri, gizli bilgi yönetimi ve zafiyet taraması kararlarını kapsar.

## Prefer

- Run as a non-root user with deterministic UID/GID when practical.
- Drop all Linux capabilities and add back only required capabilities.
- Use `read_only: true` with explicit writable mounts or `tmpfs` for temporary paths.
- Use BuildKit secrets and Compose secrets for sensitive values.
- Scan images before deployment.
- Enable `no-new-privileges` via `--security-opt no-new-privileges=true`.

## Avoid

- Do not use `privileged: true` without explicit operational justification; it grants all capabilities, all host devices, and disables seccomp/AppArmor/SELinux.
- Do not mount `/var/run/docker.sock` into application containers by default; Docker API access is equivalent to host root.
- Do not use host networking to avoid fixing service discovery.
- Do not store credentials in image layers or committed `.env` files; layers are immutable and extractable with `docker history --no-trunc`.
- Do not disable the default seccomp profile with `seccomp=unconfined`.

## Example

### Bad

```dockerfile
FROM node:20
WORKDIR /app
COPY . .
RUN npm ci
# No USER instruction -- runs as root (UID 0)
CMD ["node", "server.js"]
```

```dockerfile
# Secrets persist in image history even if deleted later
COPY credentials.json /app/
RUN ./setup.sh --config /app/credentials.json
RUN rm /app/credentials.json   # Still in the previous layer!
```

### Good

```dockerfile
# syntax=docker/dockerfile:1
FROM node:20-alpine

WORKDIR /app
COPY --chown=1001:1001 . .
RUN addgroup -g 1001 -S appgroup && adduser -u 1001 -S appuser -G appgroup \
    && npm ci --production
USER 1001:1001

RUN --mount=type=secret,id=api_key \
    cat /run/secrets/api_key | ./setup.sh --api-key-stdin

CMD ["node", "server.js"]
```

```yaml
services:
  app:
    cap_drop: [ALL]
    cap_add: [NET_BIND_SERVICE]
    security_opt: [no-new-privileges=true]
    read_only: true
    tmpfs:
      - /tmp:size=64m
```

## Verify

```bash
docker inspect <container>
docker history <image>
trivy image <image>
```

Reference: references/core-security.md, references/core-security-hardening-checklist.md, references/core-security-scanning.md, references/core-security-anti-patterns.md
