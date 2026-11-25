برای انتقال یک کلکشن Qdrant از یک داکر به داکر دیگر در سروری متفاوت، دو روش اصلی وجود دارد: استفاده از **ابزار رسمی Migration** (سریع‌تر و ساده‌تر) یا استفاده از **Snapshot** (دقیق‌تر و مناسب برای حجم‌های بزرگ). با توجه به اینکه هر دو سرور شما داکر دارند و می‌خواهید کلکشن را منتقل کنید، روش Migration با ابزار رسمی معمولاً کم‌دردسرترین گزینه است.

### 🚀 روش اول: استفاده از ابزار رسمی Qdrant Migration (پیشنهادی)

این روش داده‌ها را به صورت زنده از مبدأ به مقصد Stream می‌کند و نیازی به دانلود و آپلود دستی فایل ندارید. ابزار رسمی `qdrant-migration` این کار را خودکار انجام می‌دهد و حتی ساختار کلکشن (شامل ایندکس‌ها و تنظیمات) را در مقصد بازسازی می‌کند .

**پیش‌نیاز مهم:** این ابزار از پروتکل **gRPC** استفاده می‌کند، بنابراین باید پورت gRPC (معمولاً `6334`) روی هر دو کانتینر Qdrant در دسترس باشد. اگر پورت `6334` را در داکر خود باز نکرده‌اید، باید این کار را انجام دهید.

**دستور اجرا:** کافی است دستور زیر را روی یکی از سرورها (یا هر ماشینی که به هر دو سرور دسترسی دارد) اجرا کنید. مقادیر `source.url` و `target.url` را با آدرس‌های واقعی سرورهای خود جایگزین کنید.

```bash
docker run --net=host --rm -it registry.cloud.qdrant.io/library/qdrant-migration qdrant \
    --source.url 'http://IP_SOURCE_SERVER:6334' \
    --source.collection 'your-collection-name' \
    --target.url 'http://IP_TARGET_SERVER:6334' \
    --target.collection 'your-collection-name'
```

*   اگر روی Qdrantهای خود احراز هویت (API Key) فعال کرده‌اید، باید پارامترهای `--source.api-key` و `--target.api-key` را نیز اضافه کنید .
*   برای افزایش سرعت انتقال داده‌های حجیم، می‌توانید از پارامتر `--migration.num-workers` برای تعیین تعداد Workerهای موازی استفاده کنید .

### 📦 روش دوم: استفاده از Snapshot (پشتیبان‌گیری و بازیابی)

اگر به هر دلیلی نمی‌توانید از ابزار Migration استفاده کنید (مثلاً پورت gRPC باز نیست) یا می‌خواهید از داده‌ها یک نسخه پشتیبان فیزیکی داشته باشید، روش Snapshot گزینه مناسبی است. این روش کل داده‌ها و ایندکس‌های ساخته‌شده را در یک فایل آرشیو می‌کند .

**گام ۱: ایجاد Snapshot در سرور مبدأ**
از طریق API (پورت `6333`) یک Snapshot از کلکشن مورد نظر بگیرید:
```bash
curl -X POST 'http://IP_SOURCE_SERVER:6333/collections/your-collection-name/snapshots'
```
پس از اجرا، نام فایل Snapshot در خروجی برگردانده می‌شود.

**گام ۲: دانلود فایل Snapshot**
فایل ایجاد شده را از کانتینر مبدأ دانلود کنید. مسیر پیش‌فرض ذخیره Snapshotها در داکر `/qdrant/snapshots` است .
```bash
# کپی کردن فایل از داخل کانتینر به هاست مبدأ
docker cp <container_id_or_name>:/qdrant/snapshots/<snapshot_file_name> .
# سپس با scp به سرور مقصد منتقل کنید
scp <snapshot_file_name> user@IP_TARGET_SERVER:/path/to/destination/
```

**گام ۳: بازیابی در سرور مقصد**
فایل Snapshot را به سرور مقصد منتقل کرده و از طریق API بازیابی کنید. **نکته بسیار مهم:** به طور پیش‌فرض، Qdrant اولویت را به داده‌های موجود می‌دهد، بنابراین اگر کلکشن مقصد خالی باشد، باید پارامتر `priority` را روی `snapshot` تنظیم کنید تا داده‌های Snapshot جایگزین شوند .

```bash
# فایل را باید در مسیری قرار دهید که کانتینر مقصد به آن دسترسی دارد (یا آن را به داخل کانتینر کپی کنید)
# سپس API بازیابی را فراخوانی کنید:
curl -X PUT 'http://IP_TARGET_SERVER:6333/collections/your-collection-name/snapshots/recover' \
  -H 'Content-Type: application/json' \
  -d '{
    "location": "file:///qdrant/snapshots/<snapshot_file_name>",
    "priority": "snapshot"
  }'
```

### 💡 نکته کلیدی درباره نسخه‌ها
قبل از شروع، مطمئن شوید که نسخه Qdrant روی سرور مقصد **دقیقاً برابر یا حداکثر یک نسخه مینور بالاتر** از سرور مبدأ باشد. برای مثال، می‌توانید Snapshot یک نسخه `1.17` را روی `1.18` بازیابی کنید، اما بازیابی آن روی `1.16` یا `1.19` ممکن است با مشکل مواجه شود .




docker run --net=host --rm -it registry.cloud.qdrant.io/library/qdrant-migration qdrant \
    --source.url 'http://78.39.10.22:6334' \
    --source.collection 'assistant_knowledge1' \
    --source.api-key '992b61d895665cd63484456f34950944dd181ea656ed5e2bf2e4268dae4e96d8' \
    --target.url 'http://78.39.10.8:6334' \
    --target.collection 'assistant_knowledge1' \
    --target.api-key '992b61d895665cd63484456f34950944dd181ea656ed5e2bf2e4268dae4e96d8'