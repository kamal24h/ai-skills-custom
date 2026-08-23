# Architecture Core Rules

**Context:** Bu kural Docker'ın temel nesne modelini (image, container, network, volume) ve mimarisini (daemon, containerd, runc) kullanan her görevde uygulanır. Image ile container ayrımını, katman modelini ve kalıcılık kararlarını etkileyen tasarım seçimlerinde devreye girer.

## Prefer

- Treat images as immutable templates and containers as disposable runtime instances.
- Use volumes or bind mounts for data that must survive container removal.
- Keep build contexts small with `.dockerignore`; Docker sends the context before instructions run.
- Use digests when production reproducibility matters.
- Run one primary process per container; manage multi-service applications with Compose or an orchestrator.
- Remember that each `RUN`, `COPY`, `ADD` creates a filesystem layer while `ENV`, `USER`, `CMD` are metadata-only.

## Avoid

- Do not use `docker commit` as a production image creation workflow.
- Do not confuse `docker export/import` with `docker save/load`; export flattens image metadata and history.
- Do not assume container isolation is a VM boundary; it relies on kernel namespaces and cgroups.
- Do not treat tags as immutable pointers; `nginx:1.25` can be repointed by the registry maintainer.
- Do not store application data (databases, uploads, logs) in the container writable layer; removal deletes it.

## Example

### Bad

```bash
# Making changes inside a running container and committing them:
docker exec myapp apt-get install -y curl
docker commit myapp myapp:with-curl
```

No Dockerfile means no audit trail and no reproducibility; the layer content is opaque and CI/CD cannot rebuild it.

```bash
# Database data stored in the container layer -- all data lost when removed:
docker run -d --name postgres postgres:16
```

### Good

```dockerfile
# Pin by digest for production reproducibility
FROM nginx:1.25@sha256:a8560b36e8b8210634f77d9f7f9efd7ffa463e380b75e2e74aff4511df3ef88c
```

```bash
# Reproducible build + named volume for persistent data
docker build -t myapp:v1 .
docker run -d --name postgres \
  --mount source=pgdata,target=/var/lib/postgresql/data \
  postgres:16
```

Volume data bypasses the overlay2 union filesystem entirely, persists across `docker rm`, and can be shared between containers.

## Verify

```bash
docker inspect <container>
docker image history <image>
docker system df
```

Reference: references/core-architecture.md, references/core-architecture-concepts.md, references/core-architecture-examples.md, references/core-architecture-anti-patterns.md
