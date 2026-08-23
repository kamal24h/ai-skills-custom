# CI/CD Rules

**Context:** Bu kural image build/push pipeline'ları (GitHub Actions ve benzeri) kurarken uygulanır. Registry kimlik doğrulama, etiketleme stratejisi, cache yapılandırması ve çoklu platform build kararlarında devreye girer.

## Prefer

- Use `docker/build-push-action` with buildx for GitHub Actions workflows.
- Authenticate to Docker Hub, GHCR, or the target registry with repository secrets.
- Publish immutable tags such as commit SHA alongside semantic or branch tags.
- Use cache-from/cache-to for repeatable CI speedups.
- Build multi-platform images only when consumers need multiple architectures.
- Use `docker/metadata-action` for consistent, automatic tagging and OCI labels instead of manual tag scripts.
- Scan images before pushing; build and scan locally first, then push only if the scan passes.

## Avoid

- Do not publish only mutable tags.
- Do not print registry tokens or secrets in logs.
- Do not push images before tests and security gates pass unless the workflow clearly marks them as pre-release artifacts.
- Do not use QEMU multi-platform builds without accepting the performance tradeoff; prefer cross-compilation for compiled languages.
- Do not pass secrets via `build-args`; they are recorded in image metadata and visible via `docker history --no-trunc`.
- Do not use `--load` with multi-platform builds; manifest lists can only exist in a registry.

## Example

### Bad

```yaml
# BAD: Secret via build-arg + only mutable tag
- uses: docker/build-push-action@v6
  with:
    push: true
    tags: user/myapp:latest
    build-args: |
      NPM_TOKEN=${{ secrets.NPM_TOKEN }}
```

Build arguments are visible via `docker history --no-trunc`; anyone who pulls the image can extract them. A `latest`-only tag leaves no rollback point.

### Good

```yaml
- name: Extract metadata
  id: meta
  uses: docker/metadata-action@v5
  with:
    images: user/myapp
    tags: |
      type=semver,pattern={{version}}
      type=ref,event=branch
      type=sha,prefix=sha-

- name: Build and push
  uses: docker/build-push-action@v6
  with:
    context: .
    platforms: linux/amd64,linux/arm64
    push: ${{ github.event_name != 'pull_request' }}
    tags: ${{ steps.meta.outputs.tags }}
    labels: ${{ steps.meta.outputs.labels }}
    secrets: |
      "npm_token=${{ secrets.NPM_TOKEN }}"
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

In the Dockerfile, consume it as a mount:

```dockerfile
RUN --mount=type=secret,id=npm_token \
    NPM_TOKEN=$(cat /run/secrets/npm_token) npm ci
```

## Verify

```bash
docker buildx build --platform linux/amd64,linux/arm64 .
docker buildx imagetools inspect <image>
```

Reference: references/impl-cicd.md, references/impl-cicd-github-actions.md, references/impl-cicd-examples.md, references/impl-cicd-anti-patterns.md
