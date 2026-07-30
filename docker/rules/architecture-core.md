# Architecture Core Rules

## Prefer

- Treat images as immutable templates and containers as disposable runtime instances.
- Use volumes or bind mounts for data that must survive container removal.
- Keep build contexts small with `.dockerignore`; Docker sends the context before instructions run.
- Use digests when production reproducibility matters.

## Avoid

- Do not use `docker commit` as a production image creation workflow.
- Do not confuse `docker export/import` with `docker save/load`; export flattens image metadata and history.
- Do not assume container isolation is a VM boundary; it relies on kernel namespaces and cgroups.

## Verify

```bash
docker inspect <container>
docker image history <image>
docker system df
```
