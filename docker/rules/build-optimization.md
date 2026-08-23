# Build Optimization Rules

**Context:** Bu kural image build sürelerini ve boyutlarını optimize ederken uygulanır. Dockerfile katman sıralaması, cache davranışı, `.dockerignore` ve CI cache backend kararlarında devreye girer.

## Prefer

- Copy dependency manifests before application source.
- Install dependencies before copying high-churn source files.
- Use `.dockerignore` to exclude `.git`, dependencies, build outputs, test artifacts, secrets, and local IDE files.
- Use remote or registry cache backends in CI when build time matters.
- Order instructions from least to most frequently changed; a cache miss invalidates all subsequent layers (cascade).
- Use `--mount=type=cache` for package manager caches so downloads survive layer rebuilds.

## Avoid

- Do not send large build contexts without checking size.
- Do not invalidate dependency layers with broad early `COPY . .`.
- Do not optimize image size by removing files in later layers after adding them in earlier layers; deletion only hides the bytes.
- Do not split `apt-get update` and `apt-get install` across layers; a stale cached index can fail or install old versions.
- Do not use `--cache-to mode=min` in CI; it skips intermediate stage layers such as dependency downloads.

## Example

### Bad

```dockerfile
FROM node:20
WORKDIR /app
COPY . .              # Cache key covers ALL files; any change reinstalls deps
RUN npm install       # Reinstalls on EVERY source change
RUN npm run build
```

### Good

```dockerfile
# syntax=docker/dockerfile:1

FROM node:20-bookworm-slim AS build
WORKDIR /app

COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci --production=false

COPY . .
RUN npm run build

FROM node:20-bookworm-slim AS runtime
WORKDIR /app
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
COPY package.json ./

USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

CI'da registry cache'i `mode=max` ile kullanın ve ana dalı yedek kaynak olarak ekleyin:

```bash
docker buildx build \
  --cache-from type=registry,ref=myapp:cache-feature-123 \
  --cache-from type=registry,ref=myapp:cache-main \
  --cache-to type=registry,ref=myapp:cache-feature-123,mode=max .
```

## Verify

```bash
docker build --progress=plain .
docker buildx du
```

Reference: references/impl-build-optimization.md, references/impl-build-optimization-caching-rules.md, references/impl-build-optimization-examples.md, references/impl-build-optimization-anti-patterns.md
