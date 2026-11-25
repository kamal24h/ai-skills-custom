

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





```

