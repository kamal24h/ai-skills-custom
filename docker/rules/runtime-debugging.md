# Runtime Debugging Rules

**Context:** Bu kural çalışan veya çöken bir container'ı teşhis ederken uygulanır. Exit kodu yorumlama, OOM, port çakışması, restart loop ve kaynak tükenmesi sorunlarında sistematik araştırma sırasını belirler.

## Prefer

- Start with logs, inspect state, events, health status, resource usage, and the configured command.
- Check exit code meanings before changing images or Compose files (e.g., 137 = SIGKILL/OOM, 143 = clean SIGTERM shutdown, 127 = command not found).
- Use `docker exec` only when the container is running; inspect stopped containers instead.
- Reproduce with the smallest `docker run` or `docker compose up` command that shows the failure.
- Confirm OOM kills with `docker inspect --format='{{.State.OOMKilled}}' <container>` before raising memory limits.

## Avoid

- Do not rebuild blindly before reading the failure signal.
- Do not mask crash loops with `restart: always`; stop the container, read the last crash logs, fix the cause, then re-enable the policy.
- Do not assume port conflicts are inside the container; check host publishing too (`lsof -i :PORT`, `docker port <container>`).
- Do not use `--oom-kill-disable` without `-m`; the kernel cannot reclaim memory and random host processes get killed.

## Example

### Bad

```bash
# Guessing: rebuild and hope
docker compose build --no-cache && docker compose up -d

# Masking a crash loop instead of diagnosing it
docker update --restart always <container>
```

### Good

```bash
# 1. Read the failure signal
docker inspect --format='ExitCode={{.State.ExitCode}} OOMKilled={{.State.OOMKilled}} RestartCount={{.RestartCount}}' <container>
docker logs --tail 50 <container>

# 2. Watch for rapid restarts
docker events --filter container=<container> --filter event=start

# 3. Break the loop, diagnose, then re-enable
docker stop <container>
docker update --restart no <container>
docker logs --tail 100 <container>
# ... fix the issue ...
docker update --restart unless-stopped <container>
```

## Verify

```bash
docker logs --tail=100 <container>
docker inspect --format '{{json .State}}' <container>
docker events --since 10m
docker stats --no-stream
```

Reference: references/errors-runtime.md, references/errors-runtime-diagnostics.md, references/errors-runtime-examples.md, references/errors-runtime-anti-patterns.md
