
docker exec -it assistant-ollama ollama pull MHKetbi/DeepSeek-R1-Distill-Llama-8B-NexaQuant:latest

docker exec -it assistant-ollama ollama pull deepseek-r1:8b (successful)


Ollama (Local LLM)	http://ollama:11434
Qdrant (Vector DB)	http://qdrant:6333
PostgreSQL	postgresql://assistant_user:${POSTGRES_PASSWORD}@postgres:5432/assistant_db
Redis	redis://redis:6379


مدیریت حافظه GPU: مدل‌های DeepSeek-R1 با کوانتیزاسیون Q4_K_M برای نسخه 7B حدود 6GB VRAM و برای نسخه 14B حدود 10GB VRAM نیاز دارند. با تنظیم OLLAMA_NUM_PARALLEL=2 از اشغال بیش از حد حافظه جلوگیری کرده‌اید.

امنیت: پورت 11434 (Ollama) را هرگز مستقیماً به اینترنت باز نکنید. در docker-compose بالا، این پورت به صورت پیش‌فرض روی 0.0.0.0 تنظیم شده اما در محیط پروداکشن باید آن را به 127.0.0.1 محدود کرده و از طریق Nginx یا Traefik به عنوان Reverse Proxy با احراز هویت، سرویس‌دهی کنید.

کوانتیزاسیون: اگر فضای VRAM کافی نیست، می‌توانید از نسخه q3_K_M استفاده کنید که حجم را کمتر می‌کند اما ممکن است کمی از دقت مدل در استدلال‌های پیچیده کاسته شود.


pip install qdrant-client langchain-ollama langchain-qdrant langchain-community -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install fastapi -i https://mirror-pypi.runflare.com/simple --trusted-host mirror-pypi.runflare.com


pip install fastapi -i https://pypi.tuna.tsinghua.edu.cn/simple

تنظیم پیشفرض میرور برای پایتون

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

تنظیم میرور برای داکر
/etc/docker/daemon.json:
{
  "registry-mirrors": ["https://mirror.gcr.io"]
}




{"answer":"\nموضوع اصلی اسناد شما مربوط به **خفاش‌ها و راه‌حل‌های مربوط به سامانه مودیان**، به‌خصوص در زمینه عملیات‌های مالی مانند ارسال صورتحساب، ثبت فاکتور فروش و برگشت، و مدیریت مشکلات پیش‌ Coming soon\n起来 می‌باشد."}


