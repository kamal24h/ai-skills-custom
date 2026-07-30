# CLI Workflow Rules

## Prefer

- Use `docker inspect --format` for focused fields instead of reading large JSON manually.
- Use `docker logs --tail` and `--since` to limit noisy output.
- Use `docker system df` before pruning.
- Use `docker save/load` for preserving image metadata in offline transfer.

## Avoid

- Do not prune images, containers, networks, or volumes without confirming scope.
- Do not use `docker export/import` when tags, history, labels, or layers must be preserved.
- Do not assume `docker ps` shows stopped containers; use `docker ps -a`.

## Verify

```bash
docker ps --all
docker inspect --format '{{json .State}}' <container>
docker system df
```
