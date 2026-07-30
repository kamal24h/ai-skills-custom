# Security Hardening Rules

## Prefer

- Run as a non-root user with deterministic UID/GID when practical.
- Drop all Linux capabilities and add back only required capabilities.
- Use `read_only: true` with explicit writable mounts or `tmpfs` for temporary paths.
- Use BuildKit secrets and Compose secrets for sensitive values.
- Scan images before deployment.

## Avoid

- Do not use `privileged: true` without explicit operational justification.
- Do not mount `/var/run/docker.sock` into application containers by default.
- Do not use host networking to avoid fixing service discovery.
- Do not store credentials in image layers or committed `.env` files.

## Verify

```bash
docker inspect <container>
docker history <image>
trivy image <image>
```
