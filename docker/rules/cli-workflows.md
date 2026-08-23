# CLI Workflow Rules

**Context:** Bu kural günlük Docker CLI kullanımında (container/image yönetimi, inspect, log, temizlik, offline transfer) uygulanır. Etkileşimli hata ayıklama ve bakım komutlarının güvenli ve verimli kullanımını kapsar.

## Prefer

- Use `docker inspect --format` for focused fields instead of reading large JSON manually.
- Use `docker logs --tail` and `--since` to limit noisy output.
- Use `docker system df` before pruning.
- Use `docker save/load` for preserving image metadata in offline transfer.
- Use `--filter` and `--format` for programmatic output instead of parsing text with grep/awk.
- Verify the active daemon with `docker context ls` before running destructive commands on remote contexts.

## Avoid

- Do not prune images, containers, networks, or volumes without confirming scope.
- Do not use `docker export/import` when tags, history, labels, or layers must be preserved.
- Do not assume `docker ps` shows stopped containers; use `docker ps -a`.
- Do not run `docker exec myapp cmd1 && cmd2` without a shell wrapper; the second command runs on the host.
- Do not push a repository without an explicit tag; it pushes every local tag of that repository.

## Example

### Bad

```bash
# Blind nuclear cleanup on production
docker system prune -a --volumes -f

# export loses layers, history, tags, and CMD/ENTRYPOINT
docker export mycontainer > backup.tar
docker import backup.tar myapp:restored

# && is interpreted by the HOST shell
docker exec myapp echo "step 1" && echo "step 2"
```

### Good

```bash
# Assess first, then clean selectively
docker system df -v
docker container prune -f
docker image prune -f
docker volume ls -f dangling=true   # verify before touching volumes

# save/load preserves the exact image with all layers, tags, and metadata
docker save -o backup.tar myapp:v1.0
docker load -i backup.tar

# Wrap chained commands in a shell inside the container
docker exec myapp sh -c "echo step 1 && echo step 2"

# Focused fields instead of full JSON
docker stats --no-stream --format '{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}'
```

## Verify

```bash
docker ps --all
docker inspect --format '{{json .State}}' <container>
docker system df
```

Reference: references/syntax-cli-containers.md, references/syntax-cli-containers-commands.md, references/syntax-cli-images.md, references/syntax-cli-images-anti-patterns.md, references/syntax-cli-containers-anti-patterns.md
