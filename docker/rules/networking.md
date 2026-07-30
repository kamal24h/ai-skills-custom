# Networking Rules

## Prefer

- Use user-defined bridge networks for container-to-container DNS on one host.
- Use service names for Compose DNS, not container IP addresses.
- Publish only the ports that must be reachable from the host.
- Separate frontend and backend networks when tiers should be isolated.
- Check subnet conflicts before creating custom IPAM ranges.

## Avoid

- Do not rely on the default bridge network for multi-service applications.
- Do not use `localhost` from one container to reach another container.
- Do not expose databases to the host unless required for development.
- Do not use host networking without documenting why port publishing and service networks are insufficient.

## Verify

```bash
docker network inspect <network>
docker compose exec <service> getent hosts <target-service>
docker compose port <service> <port>
```
