# Dockerfile Basics Rules

## Prefer

- Start BuildKit Dockerfiles with `# syntax=docker/dockerfile:1`.
- Use `COPY` for local files and reserve `ADD` for archive extraction or remote sources with a reason.
- Use `WORKDIR` instead of `RUN cd`.
- Use exec form for `ENTRYPOINT` and `CMD`.
- Create and switch to a non-root `USER` in the final runtime stage.

## Avoid

- Do not use `latest` for production base images.
- Do not place secrets in `ARG`, `ENV`, or copied files.
- Do not split `apt-get update` and `apt-get install` across layers.
- Do not leave package manager caches in runtime layers.

## Verify

```bash
docker build .
docker history <image>
```
