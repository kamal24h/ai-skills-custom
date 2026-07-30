# BuildKit Mount Rules

## Prefer

- Use `RUN --mount=type=cache` for package manager caches.
- Use `RUN --mount=type=secret` for build-time credentials.
- Use `RUN --mount=type=ssh` for private repository access.
- Keep secret and SSH mounts scoped to the single `RUN` instruction that needs them.

## Avoid

- Do not pass secrets with `ARG` or `ENV`.
- Do not expect cache mounts to become part of the image.
- Do not rely on BuildKit-only syntax without a syntax directive.

## Verify

```bash
DOCKER_BUILDKIT=1 docker build --progress=plain .
```
