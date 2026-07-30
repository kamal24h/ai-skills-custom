# Build Optimization Rules

## Prefer

- Copy dependency manifests before application source.
- Install dependencies before copying high-churn source files.
- Use `.dockerignore` to exclude `.git`, dependencies, build outputs, test artifacts, secrets, and local IDE files.
- Use remote or registry cache backends in CI when build time matters.

## Avoid

- Do not send large build contexts without checking size.
- Do not invalidate dependency layers with broad early `COPY . .`.
- Do not optimize image size by removing files in later layers after adding them in earlier layers.

## Verify

```bash
docker build --progress=plain .
docker buildx du
```
