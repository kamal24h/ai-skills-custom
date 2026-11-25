

**وارد کانتینر اولاما شوید و مدل را دریافت کنید**

```bash

# نصب مدل روی اولاما
docker exec -it ollama ollama pull qwen3.5:27b
docker exec -it ollama ollama pull qwen3.5:9b
docker exec -it ollama ollama pull qllama/bge-m3:q4_k_m

# لیست مدل های روی اولاما
docker exec -it ollama ollama list

# لیست مدل های فعال روی اولاما
docker exec -it ollama ollama ps

# غیر فعال کردن مدل روی اولاما
docker exec -it ollama ollama stop qwen3.5:27b


# حذف مدل از روی اولاما
docker exec -it ollama ollama rm llama3 


# تست سرعت مدل روی اولاما

docker exec -it ollama ollama run qwen3.5:9b --verbose

# warm-up
curl -s -X POST http://localhost:11434/api/generate \
  -d '{"model":"qwen3.5:9b","prompt":"warmup","stream":false}' > /dev/null

# تست واقعی (مسیر legacy که 504 می‌داد)
time curl -X POST http://127.0.0.1:8000/api/v1/conversations/5c39f741-ed43-41f0-97b4-855e0194ebf1/messages \
  -H "X-API-Key:23594e809049550a06c32aa1bf1fc59ee028d170c556e0780e9c34bb665bf3ce" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"سلام","tenantId":"119","userId":"119"}' \
  -w "\nHTTP: %{http_code}  TOTAL: %{time_total}s\n"


```

