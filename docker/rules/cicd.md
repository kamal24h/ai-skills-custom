# CI/CD Rules

## Prefer

- Use `docker/build-push-action` with buildx for GitHub Actions workflows.
- Authenticate to Docker Hub, GHCR, or the target registry with repository secrets.
- Publish immutable tags such as commit SHA alongside semantic or branch tags.
- Use cache-from/cache-to for repeatable CI speedups.
- Build multi-platform images only when consumers need multiple architectures.

## Avoid

- Do not publish only mutable tags.
- Do not print registry tokens or secrets in logs.
- Do not push images before tests and security gates pass unless the workflow clearly marks them as pre-release artifacts.
- Do not use QEMU multi-platform builds without accepting the performance tradeoff.

## Verify

```bash
docker buildx build --platform linux/amd64,linux/arm64 .
docker buildx imagetools inspect <image>
```
