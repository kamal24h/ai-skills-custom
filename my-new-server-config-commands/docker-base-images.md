

# services

**---------- LLM (Ollama) ----------**
  ```bash
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    restart: unless-stopped
    volumes:
      - ollama_data:/root/.ollama
    ports:
      - "11434:11434"
    environment:
      - OLLAMA_HOST=0.0.0.0
      - OLLAMA_NUM_PARALLEL=1
      - OLLAMA_MAX_LOADED_MODELS=1
      - NVIDIA_VISIBLE_DEVICES=all
      - OLLAMA_KEEP_ALIVE=-1
      - NVIDIA_DRIVER_CAPABILITIES=compute,utility
    gpus: all
    networks:
      - assistant_network
  ```

**---------- Vector DB (Qdrant) ----------**

  ```bash
  qdrant:
    image: qdrant/qdrant:v1.20
    container_name: assistant-qdrant
    restart: unless-stopped
    volumes:
      - qdrant_data:/qdrant/storage
    ports:
      - "6333:6333"
      - "6334:6334"
    environment:
      - QDRANT__SERVICE__GRPC_PORT=6334
      - QDRANT__SERVICE__API_KEY=${QDRANT_API_KEY}
    networks:
      - assistant_network
  ```

**---------- Relational DB (PostgreSQL) ----------**
  
  ```bash
  postgres:
    image: postgres:16-alpine
    container_name: assistant-postgres
    restart: unless-stopped
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-assistant_user}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB:-assistant_db}
    healthcheck:
      test:
        - CMD-SHELL
        - pg_isready -U ${POSTGRES_USER:-assistant_user} -d ${POSTGRES_DB:-assistant_db}
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - assistant_network
  ```
    
**---------- Cache (Redis) ----------**
  
  ```bash
  redis:
    image: redis:7-alpine
    container_name: assistant-redis
    restart: unless-stopped
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes --maxmemory 256mb --maxmemory-policy allkeys-lru
    networks:
      - assistant_network
  ```

**---------- Queue (RabbitMQ) ----------**

  ```bash
  rabbitmq:
    image: docker.arvancloud.ir/rabbitmq:3.13-management
    container_name: rabbitmq
    restart: unless-stopped
    ports:
      - "5672:5672"     # AMQP
      - "15672:15672"   # Management UI
    environment:
      RABBITMQ_DEFAULT_USER: admin
      RABBITMQ_DEFAULT_PASS: admin
    volumes:
      - ./rabbit/data:/var/lib/rabbit
    networks:
      - assistant_network
  ```

  **---------- Secure Passes (Vault) ----------**

  ```bash
  vault:
    image: docker.arvancloud.ir/hashicorp/vault:1.16
    container_name: vault
    restart: unless-stopped
    cap_add:
      - IPC_LOCK
    ports:
      - "8200:8200"
    volumes:
      - ./vault/config:/vault/config
      - ./vault/data:/vault/data
      - ./vault/logs:/vault/logs
    environment:
      VAULT_LOCAL_CONFIG: |
        {
          "listener": [{
            "tcp": {
              "address": "0.0.0.0:8200",
              "tls_disable": true
            }
          }],
          "storage": {
            "file": {
              "path": "/vault/data"
            }
          },
          "ui": true,
          "disable_mlock": false,
          "api_addr": "http://78.39.10.8:8200",
          "cluster_addr": "http://78.39.10.8:8201"
        }
    command: ["server"]
    networks:
      - assistant_network
  ```

**---------- Persistent Volumes ----------**

```bash
volumes:
  ollama_data:
    external: true
    name: ollama

  qdrant_data:
  postgres_data:
  redis_data:
```

**---------- Shared Network ----------**

```bash
networks:
  assistant_network:
    external: true
```
