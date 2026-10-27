
**بیلد عادی fastApi**
```bash
docker compose build fastapi
docker compose up -d fastapi
```

**بیلد بدون کش fastApi**
```bash
docker compose build --no-cache fastapi
docker compose up -d fastapi
```

**کانتینرهای روی داکر با فرمت شخصی سازی شده**
```bash
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
```

**لیست کتابخانه های روی داکر برای fastapi**
```bash
docker exec -it fastapi_backend pip list
```

**چک کردن لاگ های fastapi**
```bash
docker logs fastapi_backend --tail=50
```

**باید مقدار API Key شما را برگرداند**
```bash
docker exec assistant-qdrant env | grep QDRANT__SERVICE__API_KEY
```

**نصب افزونه pgvector در کانتینر PostgreSQL**
```bash
docker exec -it assistant-postgres psql -U assistant_user -d assistant_db -c "CREATE EXTENSION IF NOT EXISTS vector;"
```


**وارد کانتینر Ollama شوید و مدل را دریافت کنید**
```bash
docker exec -it assistant-ollama ollama pull deepseek-r1:7b-q4_K_M
```

**وارد کانتینر Ollama شوید و لیست مدل را دریافت کنید**
```bash
docker exec -it assistant-ollama ollama list
```

**ریست و اجرای جدید داکرها**
```bash
docker compose down
docker compose up -d
docker compose ps
docker logs fastapi_backend --tail=30
curl http://127.0.0.1:8000/health
```

**بالا آوردن یکی از داکر کانتینرها**
```bash
docker compose up -d fastapi
```

**بیلد و بالا آوردن همه داکر کانتینرها**
```bash
docker compose up -d --build
```


# کار با دیتابیس اصلی روی داکر

**بکاپ**
```bash
docker exec assistant-postgres pg_dump -U assistant_user assistant_db > backup.sql
```

**ری‌استور**
```bash
docker exec -i assistant-postgres psql -U assistant_user -d assistant_db < backup.sql
```

**تغییر رمز دیتابیس**

```bash
docker exec -it assistant-postgres psql -U assistant_user -d assistant_db

ALTER USER assistant_user WITH PASSWORD 'aRianaSsist2026';
\q
```

**چک کردن اندازه سایز وکتور در qdrant**
```bash
docker exec -it fastapi_backend python -c "
from qdrant_client import QdrantClient
from config import settings
c = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key or None)
for col in c.get_collections().collections:
    info = c.get_collection(col.name)
    print(f'{col.name} -> dim: {info.config.params.vectors.size} | points: {info.points_count}')
"
```


**بازسازی ایمیج و ری‌استارت**
```bash
docker compose up -d --build
```

**یا اگر اسم سرویس را می‌دانی**
```bash
docker compose up -d --build fastapi
```

**مشاهده لاگ‌ها برای اطمینان از بالا آمدن**
```bash
docker compose logs -f fastapi --tail=30
```
**بازسازی ایمیج برنامه و ری‌استارت**

```bash
docker compose build fastapi
docker compose up -d --no-deps fastapi
docker logs -f fastapi_backend
```

**چک سینتکس بدون اجرا**
```bash
python -m py_compile services/conversation_service.py
```
