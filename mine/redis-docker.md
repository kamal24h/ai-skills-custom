
# Connect to REDIS over Docker
```bash
docker exec -it assistant-redis redis-cli
docker exec -it assistant-redis redis-cli -a YOUR_PASSWORD

redis-cli -h 127.0.0.1 -p 6379
redis-cli -h 127.0.0.1 -p 6379 -a YOUR_PASSWORD
```

# Redis-cli Commands
```bash
Role // master|slave
REPLICAOF NO ONE // to disable replica and be master
```