
# دستورات کنترلی روی سرور برای نظارت بر اجرای صحیح سرور لینوکس دستیار

**بررسی عادی سرور و اجرای دستورات زیر به ترتیب**
```bash
docker compose logs ollama | head -30
docker compose logs fastapi | head -30
```



**اگر این مورد جواب ندهد یعنی داکر به گرافیک دسترسی ندارد**
```bash
docker compose exec ollama nvidia-smi

nvidia-smi

sudo systemctl restart docker
cd /opt/assist
docker compose down
docker compose up -d


```

**لیست کتابخانه های روی داکر برای fastapi**
```bash
docker exec -it fastapi_backend pip list
```

**ریست و اجرای جدید داکرها**
```bash
docker compose down 
docker compose up -d
docker compose ps
docker logs fastapi_backend --tail=30
curl http://127.0.0.1:8000/health
```

**ریست و اجرای جدید داکرها**
```bash
docker compose exec ollama ollama run qwen3.5:9b "سلام، خوبی؟" --think=false
```


curl http://localhost:11434/api/generate -d '{"model":"qwen3.5:9b","prompt":"Hello","stream":false}'
