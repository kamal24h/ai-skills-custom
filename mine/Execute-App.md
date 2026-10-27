
cd /opt/assistant/

**فعال کردن شبکه داخلی داکر**
docker network create rag_assistant.conf 2>/dev/null || true
result:
d84fa0eda02fe982e28e7cf14ca456de85332c649bbb1a0a06364883ef578f95

**فعالسازی مجدد nginx**
sudo ln -s /etc/nginx/sites-available/rag_assistant.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

**کانفیگ انجین ایکس**
sudo ln -s /etc/nginx/sites-available/rag_assistant.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

docker compose up -d --build

**تست سلامت مستقیم FastAPI از داخل سرور:**
curl http://127.0.0.1:8000/health
**تست از طریق Nginx:**
curl http://localhost/health


docker compose build --no-cache fastapi

**تست اتصال به ردیس اگر که رمز داده باشم.**
docker exec -it assistant-redis redis-cli -a "YourStrongPasswordHere" ping



python3 -m venv venv && source venv/bin/activate

python ingest.py

uvicorn main:app --reload --port 8000


curl -X POST http://localhost:8000/query \
     -H "Content-Type: application/json" \
     -d '{"prompt": "What is the main topic of my documents?"}'


curl http://localhost:11434/api/chat -d '{
  "model": "deepseek-r1:8b",
  "messages": [{"role": "user", "content": "سلام"}],
  "stream": false
}'

curl -X POST http://127.0.0.1:8000/query -H "Content-Type: application/json" -d '{"prompt": "چرا هنگام ثبت فاکتور برگشت از فروش، فاکتور مرجع قابل مشاهده نیست؟"}'

 curl -X POST http://127.0.0.1:8000/query -H "Content-Type: application/json" -d '{"prompt": "چرا هنگام ثبت فاکتور برگشت از فروش، فاکتور مرجع قابل مشاهده نیست؟"}'
{"answer":"According to the context, the answer is:\n\nوضعیت فاکتور اصلی در بخش جمع آوری و ارسال صورتحساب باید در بخش ارسال شده موفق ها باشد تا بتوانید از روی آن فاکتور برگشت از فروش مودیان را ایجاد کنید."}(venv) arisa@arisa-X399-AORUS-PRO:/opt/assistant$


 curl -X POST http://127.0.0.1:8000/query -H "Content-Type: application/json" -d '{"prompt": "چرا فاکتور ارسال شده خطای شماره اقتصادی فروشنده با اطلاعات سامانه منطبق نیست دریافت کرده است؟"}'

curl -X POST http://127.0.0.1:8000/query \
  -H "Content-Type: application/json" \
  -d '{"prompt": "علت خطای \"532462766- exit code:\" هنگام ارسال صورتحساب برای چیست؟"}'

curl -X POST http://127.0.0.1:8000/query \:8000/query \
  -H "Content-Type: application/json" \
  -d '{"prompt": "علت خطای \"532462766- exit code:\" هنگام ارسال صورتحساب برای چیست؟"}'

{"answer":"The answer is: این خطا بعلت غیرفعال شدن شناسه یکتای حافظه مالیاتی در کارپوشه سامانه مودیان است که برای رفع آن کافیست دوباره از فرم تنظیمات سامانه مودیان بر روی گزینه \"دانلود کلید عمومی\" کلیک و فایل \"pub\" دانلود شده را در مسیر کارپوشه مودیان مالیاتی قرار دهید تا مجدد ارتباط نرم افزار با سامانه مودیان برقرار شود."}

curl -X POST http://127.0.0.1:8000/query \:8000/query \
  -H "Content-Type: application/json" \
  -d '{"prompt": "ارسال فاکتور به سامانه مودیان رمز خود را فراموش کردید ؟"}'


  "prompt": "فاکتور مرجع در فاکتور برگشت از فروش"
   "answer": "پاسخ 13:\n\nچرا فاکتور ارسال شده خطای \"تاریخ و زمان صدور صورتحساب میلادی با قواعد محاسباتی منطبق نیست\" دریافت کرده است؟\n\nوارد نمی شدم."