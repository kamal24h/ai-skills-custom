برای مشاهده محتوا، کالکشن‌ها و رکوردهای ذخیره‌شده (Points/Vectors/Payloads) در Qdrant، سه روش کاربردی و استاندارد وجود دارد:

---

### ۱. استفاده از داشبورد گرافیکی وب (Qdrant Web UI) — ساده‌ترین روش

دیتابیس Qdrant یک داشبورد وب داخلی دارد که مستقیماً روی پورت **6333** اجرا می‌شود.

#### مراحل باز کردن:

1. مرورگر خود را باز کنید و آدرس زیر را وارد نمایید:
```text
http://<SERVER_PUBLIC_IP>:6333/dashboard

```


2. **احراز هویت:**
چون در `docker-compose.yml` شما برای Qdrant کلید `api_key` فعال شده است， داشبورد از شما **API-Key** می‌خواهد. مقدار کلید را از فایل خود وارد کنید:


```text
992b61d895665cd63484456f34950944dd181ea656ed5e2bf2e4268dae4e96d8

```


3. پس از ورود:
* کالکشن `assistant_knowledge1` را انتخاب کنید.


* در تب **Points / Visualizer** می‌توانید متن چانک‌ها، متادیتاها (`doc_id`, `app_id`, `version`) و مشخصات وکتورها را به صورت گرافیکی مشاهده و جستجو کنید.



> **نکته امنیتی/دسترسی:** اگر پورت 6333 در فایروال سرور (UFW یا پنل ابری) مسدود است، می‌توانید با یک تونل SSH ساده از سیستم محلی خود به آن متصل شوید:
> ```bash
> ssh -L 6333:localhost:6333 user@SERVER_IP
> 
> ```
> 
> 
> سپس در مرورگر سیستم خود `http://localhost:6333/dashboard` را باز کنید.

---

### ۲. مشاهده از طریق اسکریپت پایتون (با `qdrant_client`)

می‌توانید یک اسکریپت سریع با استفاده از کلاینت پایتون اجرا کنید تا ۱۰ رکورد آخر کالکشن همراه با متن و متادیتای ذخیره‌شده را برایتان پرینت کند:

```python
# view_qdrant.py
from qdrant_client import QdrantClient

QDRANT_URL = "http://localhost:6333"  # یا در محیط سرور
API_KEY = "992b61d895665cd63484456f34950944dd181ea656ed5e2bf2e4268dae4e96d8"
COLLECTION_NAME = "assistant_knowledge1"

client = QdrantClient(url=QDRANT_URL, api_key=API_KEY)

# 1. دریافت اطلاعات کلی کالکشن (تعداد وکتورها و وضعیت)
info = client.get_collection(collection_name=COLLECTION_NAME)
print(f"📊 تعداد کل وکتورها: {info.points_count}")
print(f"📐 وضعیت کالکشن: {info.status}\n")

# 2. اسکرول و خواندن ۵ نمونه رکورد
records, next_page = client.scroll(
    collection_name=COLLECTION_NAME,
    limit=5,
    with_payload=True,
    with_vectors=False # برای شلوغ نشدن خروجی، آرایه اعداد برداری را خاموش می‌کنیم
)

for idx, record in enumerate(records, 1):
    print(f"--- رکورد {idx} (ID: {record.id}) ---")
    payload = record.payload or {}
    print(f"📄 سند: {payload.get('doc_name')} | برنامه: {payload.get('app_id')}")
    print(f"📝 متن چانک (100 کاراکتر اول): {payload.get('page_content', '')[:100]}...")
    print(f"🏷️ متادیتا: {payload.get('metadata')}\n")

```

---

### ۳. استفاده از cURL یا Postman (REST API)

می‌توانید مستقیماً اندپوینت اسکرول دیتابیس را فراخوانی کنید:

```bash
curl -X POST "http://localhost:6333/collections/assistant_knowledge1/points/scroll" \
     -H "api-key: 992b61d895665cd63484456f34950944dd181ea656ed5e2bf2e4268dae4e96d8" \
     -H "Content-Type: application/json" \
     -d '{
       "limit": 3,
       "with_payload": true,
       "with_vector": false
     }'

```