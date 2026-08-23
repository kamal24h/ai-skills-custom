# Networking Rules

**Context:** Bu kural container'lar arası iletişim ve host'a port yayınlama tasarlanırken uygulanır. Network driver seçimi, DNS keşfi, çok katmanlı izolasyon ve IPAM kararlarında devreye girer.

## Prefer

- Use user-defined bridge networks for container-to-container DNS on one host.
- Use service names for Compose DNS, not container IP addresses.
- Publish only the ports that must be reachable from the host.
- Separate frontend and backend networks when tiers should be isolated.
- Check subnet conflicts before creating custom IPAM ranges.

## Avoid

- Do not rely on the default bridge network for multi-service applications; it has no automatic DNS and no isolation between unrelated containers.
- Do not use `localhost` from one container to reach another container; each container has its own network namespace.
- Do not expose databases to the host unless required for development.
- Do not use host networking without documenting why port publishing and service networks are insufficient; it removes isolation entirely.
- Do not publish ports for container-to-container traffic only; containers on the same user-defined network already reach all ports.

## Example

### Bad

```bash
# Default bridge: NO DNS resolution -- connection fails
docker run -d --name db postgres:16
docker run -d --name api -e DB_HOST=db myapi
# api CANNOT resolve "db" by name

# Exposes the database to every interface
docker run -d -p 5432:5432 postgres:16
```

### Good

```bash
docker network create app-net

# No -p for inter-container communication
docker run -d --name db --network app-net postgres:16
docker run -d --name api --network app-net -e DB_HOST=db myapi

# Publish only what external clients need, bound to localhost
docker run -d --name api-pub --network app-net -p 127.0.0.1:3000:3000 myapi
```

```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    networks:
      - frontend
  db:
    image: postgres:16
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    internal: true
```

## Verify

```bash
docker network inspect <network>
docker compose exec <service> getent hosts <target-service>
docker compose port <service> <port>
```

Reference: references/core-networking.md, references/core-networking-drivers.md, references/core-networking-examples.md, references/core-networking-anti-patterns.md
