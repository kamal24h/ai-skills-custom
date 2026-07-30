# Production Readiness Rules

## Prefer

- Use minimal runtime images such as slim, alpine, distroless, or scratch when compatible.
- Add a health check that verifies actual readiness.
- Configure restart policy, resource limits, and log rotation.
- Use OCI labels for image metadata.
- Pin base images by digest where reproducibility is required.

## Avoid

- Do not ship SDKs, compilers, package caches, or test tooling in runtime images.
- Do not run production services without memory and CPU limits.
- Do not use shell-form entrypoints that swallow signals.
- Do not write logs only inside the container filesystem.

## Verify

```bash
docker inspect <container>
docker stats --no-stream
docker scout cves <image>
```
