# Runtime Debugging Rules

## Prefer

- Start with logs, inspect state, events, health status, resource usage, and the configured command.
- Check exit code meanings before changing images or Compose files.
- Use `docker exec` only when the container is running; inspect stopped containers instead.
- Reproduce with the smallest `docker run` or `docker compose up` command that shows the failure.

## Avoid

- Do not rebuild blindly before reading the failure signal.
- Do not mask crash loops with `restart: always`.
- Do not assume port conflicts are inside the container; check host publishing too.

## Verify

```bash
docker logs --tail=100 <container>
docker inspect --format '{{json .State}}' <container>
docker events --since 10m
docker stats --no-stream
```
