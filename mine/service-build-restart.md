# راه‌اندازی مجدد سرویس پایتونی پس از تغییرات

## گام‌به‌گام

### ۱. بررسی syntax قبل از build

قبل از هر چیز، مطمئن شو فایل `main.py` از نظر سینتکس سالم است:

```bash
cd /path/to/project
python3 -c "import ast; ast.parse(open('src/assistant_api/app/main.py').read()); print('OK')"
```

**انتظار:** `OK`

اگر خطا داد، باید اصلاح شود.

---

### ۲. Build مجدد image

```bash
docker compose build assistant
```

**انتظار:** `Successfully built ...`

**اگر خطا داد:**
- `python-multipart` در `requirements.txt` هست؟ (که در گام قبل اضافه کردیم)
- پکیج جدیدی import کردی که نصب نیست؟ (مثل `Literal` که از `typing` است — بدون نیاز به نصب)

**نکته:** build فقط `assistant` را می‌سازد، نه `coordinator`/`rag` را. زمان: ~۳۰ ثانیه (چون requirements تغییر نکرد، فقط لایه‌ی `COPY app` invalidate می‌شود).

---

### ۳. restart container

دو راه:

**راه A (توصیه): `up -d --no-deps`**
```bash
docker compose up -d --no-deps assistant
```

**`--no-deps`** یعنی: فقط `assistant` را restart کن، به dependencyها (`coordinator`, `rag`) دست نزن.

**مزایا:**
- `coordinator` و `rag` restart نمی‌شوند (uptime حفظ).
- سریع.
- اگر `depends_on` با `condition: service_healthy` داری، Compose آن را نادیده می‌گیرد (چون `--no-deps`).

**راه B (اگر `--no-deps` کار نکرد):**
```bash
docker compose stop assistant
docker compose rm -f assistant
docker compose up -d assistant
```

**یا معادل:**
```bash
docker compose up -d --force-recreate assistant
```

**راه C (خیلی ساده):**
```bash
docker compose restart assistant
```

**⚠️ هشدار:** `restart` **image را عوض نمی‌کند!** فقط container موجود را restart می‌کند با image قبلی. اگر `build` را زدی، `restart` image جدید را استفاده **نمی‌کند**. باید `up -d` بزنی.

**پس:** راه A توصیه می‌شود.

---

### ۴. تأیید

#### T-1: container سالم است

```bash
docker compose ps assistant
# انتظار: Up ... (healthy)
```

#### T-2: لاگ بدون خطا

```bash
docker compose logs assistant --tail 30
# انتظار: Application startup complete. Uvicorn running on http://0.0.0.0:8100
# بدون Traceback
```

#### T-3: health از اینترنت

```bash
curl -s http://78.39.10.22:8080/health | jq
# انتظار: {"status": "healthy", ...}
```

#### T-4: OpenAPI شامل endpointهای جدید

```bash
curl -s http://78.39.10.22:8080/openapi.json | jq '.paths | keys' | sort
```

**انتظار** (باید این‌ها را ببینی):
```
[
  "/api/v1/assistant/chat",
  "/api/v1/assistant/chat/stream",
  "/api/v1/conversations",
  "/api/v1/conversations/{conversation_id}",
  "/api/v1/conversations/{conversation_id}/feedback",
  "/api/v1/conversations/{conversation_id}/messages",              ← برگشته
  "/api/v1/conversations/{conversation_id}/messages/{message_id}/liked",
  "/api/v1/documents",
  "/api/v1/documents/app-ids",
  "/api/v1/documents/by-app/{app_id}",
  "/api/v1/documents/by-logical/{logical_doc_id}",
  "/api/v1/documents/by-logical/{logical_doc_id}/versions",
  "/api/v1/documents/create",
  "/api/v1/documents/create-text",
  "/api/v1/documents/create-text2",
  "/api/v1/documents/{document_id}",
  "/api/v1/erp/approvals/{approval_id}",
  "/api/v1/erp/approvals/{approval_id}/approve",
  "/api/v1/erp/approvals/{approval_id}/reject",
  "/health"
]
```

**نکته:** `POST /conversations` و `POST /conversations/{id}/messages` باید در لیست باشند.

#### T-5: سازگاری با کلاینت قدیمی (بدون تغییر)

**ساخت conversation (endpoint قدیمی):**
```bash
curl -s -X POST http://78.39.10.22:8080/api/v1/conversations \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $ASSISTANT_API_KEY" \
  -d '{"appId":"erp","tenantId":"t1","userId":"u1"}' | jq
```

**انتظار:** `{"id":"...","app_id":"erp",...}` — همان ساختار قبلی. ✅

**ارسال پیام (endpoint قدیمی):**
```bash
CONV=$(<از T-5>)
curl -s -X POST "http://78.39.10.22:8080/api/v1/conversations/$CONV/messages" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $ASSISTANT_API_KEY" \
  -d '{"prompt":"سلام، خوبی؟","tenantId":"t1","userId":"u1"}' | jq
```

**انتظار:** همان ساختار `MessageOut` قبلی:
```json
{
  "id": "...",
  "conversation_id": "...",
  "query": "سلام، خوبی؟",
  "answer": "...",
  "duration": null,
  "error": null,
  "meta_info": {
    "status": "completed",
    "selectedPath": "local_llm",
    "sources": []
  },
  "liked": null,
  "created_at": null,
  "role": null,
  "content": null
}
```

**کلاینت قدیمی بدون هیچ تغییری کار می‌کند.** ✅

#### T-6: قابلیت‌های جدید

**Chat جدید:**
```bash
curl -s -X POST http://78.39.10.22:8080/api/v1/assistant/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $ASSISTANT_API_KEY" \
  -d '{"appId":"erp","tenantId":"t1","userId":"u1","prompt":"سلام"}' | jq '.status, .selectedPath'
```

**انتظار:** `"completed"`, `"local_llm"`.

**SSE:**
```bash
curl -N -X POST http://78.39.10.22:8080/api/v1/assistant/chat/stream \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $ASSISTANT_API_KEY" \
  -d '{"appId":"erp","tenantId":"t1","userId":"u1","prompt":"یک جمله بگو"}'
```

**انتظار:** eventها یکی‌یکی (نه یک‌جا).

---

## ۵. اگر build سریع شکست خورد

معمولاً یا `requirements.txt` ناقص است یا کد syntax error دارد. این را چک کن:

```bash
# build با لاگ کامل
docker compose build --no-cache --progress=plain assistant 2>&1 | tail -50
```

**اگر خطای `ModuleNotFoundError` بود:** در `src/assistant_api/requirements.txt` پکیج گم‌شده را اضافه کن.

**اگر خطای `SyntaxError` بود:** در `main.py` خط گزارش‌شده را چک کن.

**اگر خطای `pip` بود:** احتمالاً مشکل mirror Tsinghua (شبکه). می‌توانی موقتاً `PIP_INDEX_URL` را override کنی:
```bash
docker compose build --build-arg PIP_INDEX_URL=https://pypi.org/simple assistant
```
(ولی نیاز به تغییر Dockerfile دارد تا `ARG` را بپذیرد. اگر لازم شد، بگو.)

---

## ۶. اگر health برنگشت

```bash
docker compose logs assistant --tail 50
```

**خطاهای رایج:**

| خطا | راه‌حل |
|---|---|
| `ModuleNotFoundError: No module named 'multipart'` | `python-multipart` در requirements نیست — اضافه کن |
| `ImportError: cannot import name 'X'` | import اشتباه در main.py |
| `Address already in use` | container قبلی هنوز بالاست — `docker compose rm -f assistant` |
| `coordinator: GetAddrInfo` | `coordinator` بالا نیست — `docker compose up -d coordinator` |
| `502 Bad Gateway` از nginx | `assistant` هنوز healthy نیست — چند ثانیه صبر کن و دوباره چک کن |

---

## ۷. چک‌لیست نهایی

- [ ] `python3 -c "import ast; ..."` → OK
- [ ] `docker compose build assistant` → موفق
- [ ] `docker compose up -d --no-deps assistant` → موفق
- [ ] `docker compose ps assistant` → `Up (healthy)`
- [ ] `docker compose logs assistant --tail 30` → بدون Traceback
- [ ] `curl http://78.39.10.22:8080/health` → healthy
- [ ] `curl http://78.39.10.22:8080/openapi.json | jq '.paths | keys'` → شامل `POST /messages`
- [ ] T-5 (کلاینت قدیمی) → همان پاسخ قبلی
- [ ] T-6 (کلاینت جدید) → پاسخ غنی‌تر

---

## ۸. یک دستور برای همه

اگر می‌خواهی همه در یک خط:

```bash
python3 -c "import ast; ast.parse(open('src/assistant_api/app/main.py').read())" && \
docker compose build assistant && \
docker compose up -d --no-deps assistant && \
sleep 3 && \
docker compose ps assistant && \
curl -s http://127.0.0.1:8100/health | jq
```

اگر خروجی `healthy` بود، موفق.

---
