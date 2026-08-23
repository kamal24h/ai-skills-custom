# Storage Rules

**Context:** Bu kural container verilerinin nerede ve nasıl tutulacağına karar verirken uygulanır. Volume tipi seçimi (named volume, bind mount, tmpfs), yedekleme ve temizlik güvenliği konularını kapsar.

## Prefer

- Use named volumes for database and durable application data.
- Use bind mounts when the container must access specific host files during development.
- Use `tmpfs` for sensitive or disposable runtime data; it lives in RAM and is never written to disk.
- Document backup and restore commands for important volumes.
- Mount read-only when the workload only needs reads.
- Prefer `--mount` syntax for bind mounts: a missing host path errors instead of being silently auto-created.

## Avoid

- Do not store durable data only in the writable container layer.
- Do not use anonymous volumes for important persistence; they have random hash names and `docker volume prune` removes them.
- Do not bind mount host paths into production without ownership and permission review; UID/GID mismatches can break access.
- Do not prune volumes before confirming data ownership and backups.
- Do not rely on volume auto-population for critical data; initialize volumes explicitly.

## Example

### Bad

```bash
# Database data in the container layer -- lost on removal
docker run -d --name postgres postgres:16
```

```yaml
# WRONG -- anonymous volume, recreated on compose down
services:
  db:
    image: postgres
    volumes:
      - /var/lib/postgresql/data
```

### Good

```bash
docker run -d --name postgres \
  --mount source=pgdata,target=/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:16

# Backup the named volume with a helper container
docker run --rm \
  --mount source=pgdata,target=/data,readonly \
  -v $(pwd):/backup \
  alpine tar czf /backup/pgdata-backup.tar.gz -C /data .

# Restore into a fresh volume
docker run --rm \
  --mount source=pgdata-restored,target=/data \
  -v $(pwd):/backup \
  alpine sh -c "cd /data && tar xzf /backup/pgdata-backup.tar.gz"
```

```yaml
services:
  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

## Verify

```bash
docker volume ls
docker volume inspect <volume>
docker inspect <container>
```

Reference: references/impl-storage.md, references/impl-storage-mount-types.md, references/impl-storage-examples.md, references/impl-storage-anti-patterns.md
