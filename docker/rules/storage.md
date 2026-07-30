# Storage Rules

## Prefer

- Use named volumes for database and durable application data.
- Use bind mounts when the container must access specific host files during development.
- Use `tmpfs` for sensitive or disposable runtime data.
- Document backup and restore commands for important volumes.
- Mount read-only when the workload only needs reads.

## Avoid

- Do not store durable data only in the writable container layer.
- Do not use anonymous volumes for important persistence.
- Do not bind mount host paths into production without ownership and permission review.
- Do not prune volumes before confirming data ownership and backups.

## Verify

```bash
docker volume ls
docker volume inspect <volume>
docker inspect <container>
```
