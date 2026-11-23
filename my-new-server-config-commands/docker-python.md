
**چک سینتکس بدون اجرا**
```bash
python -m py_compile services/conversation_service.py
```

**بازسازی ایمیج برنامه و ری‌استارت**

```bash
docker compose build assist
docker compose up -d --no-deps assist
docker compose up -d --build --no-deps assist
# لاگ زنده
docker logs -f assist-image-name --tail=30 
# لاگ به تعداد ردیف مشخص تاکنون
docker compose logs assist-service-name --tail=30 
```


# نصب Python و ابزارهای موردنیاز
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv python3-dev

# بررسی نسخه
python3 --version
pip3 --version

# ایجاد محیط مجازی
python3 -m venv venv

# فعال‌سازی محیط مجازی
source venv/bin/activate

# به‌روزرسانی pip
pip install --upgrade pip

# نصب FastAPI و Uvicorn
pip install fastapi "uvicorn[standard]"

# بررسی نصب
pip show fastapi uvicorn
```

