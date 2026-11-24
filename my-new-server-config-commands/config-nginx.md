
برای دسترسی به یک اپلیکیشن وب که روی داکر اجرا می‌شود از خارج سرور، رایج‌ترین و امن‌ترین روش استفاده از **Nginx به عنوان Reverse Proxy** روی خود سرور اوبونتو است. در این معماری، Nginx ترافیک ورودی پورت‌های 80 و 443 را دریافت کرده و آن را به پورت داخلی کانتینر داکر هدایت می‌کند. این کار باعث می‌شود پورت اپلیکیشن مستقیماً به اینترنت باز نباشد.

### 1. پیش‌نیازها و آماده‌سازی سرور

ابتدا مطمئن شوید که به سرور دسترسی SSH دارید و پورت‌های لازم در فایروال (و در صورت استفاده از سرور ابری، در Security Group) باز شده‌اند.

```bash
# به‌روزرسانی لیست پکیج‌ها
sudo apt update

# نصب Nginx
sudo apt install nginx -y

# بررسی وضعیت سرویس (باید Active باشد)
sudo systemctl status nginx
```

پس از نصب، باید پورت‌های **80 (HTTP)** و **443 (HTTPS)** را در فایروال باز کنید. اگر از `ufw` استفاده می‌کنید:

```bash
sudo ufw allow 'Nginx Full'
# یا به صورت دستی:
# sudo ufw allow 80/tcp
# sudo ufw allow 443/tcp
sudo ufw enable
```


### 2. آماده‌سازی اپلیکیشن داکر

فرض کنید اپلیکیشن وب شما در داکر روی پورت داخلی `8080` (یا هر پورت دیگری) در حال اجرا است. **نکته مهم** این است که هنگام اجرای کانتینر، پورت را فقط به لوکال‌هاست (`127.0.0.1`) بایند کنید تا از دسترسی مستقیم خارجی به آن جلوگیری شود. Nginx روی خود سرور می‌تواند به این پورت دسترسی داشته باشد.

```bash
# مثال اجرای کانتینر با بایند به لوکال‌هاست
docker run -d \
  --name my-web-app \
  --restart always \
  -p 127.0.0.1:8080:80 \
  my-web-app-image
```


### 3. پیکربندی Nginx (Reverse Proxy)

فایل کانفیگ جدیدی در مسیر `sites-available` ایجاد کنید.

```bash
sudo nano /etc/nginx/sites-available/my-web-app
```

محتوای زیر را وارد کنید (فرض بر این است که دامنه شما `app.example.com` است و اپلیکیشن روی `127.0.0.1:8080` گوش می‌دهد):

```nginx
server {
    listen 80;
    listen [::]:80;

    # دامنه یا ساب‌دامنه خود را جایگزین کنید
    server_name app.example.com;

    location / {
        # هدایت به اپلیکیشن داکر روی لوکال‌هاست
        proxy_pass http://127.0.0.1:8080;

        # ارسال هدرهای ضروری به اپلیکیشن
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # برای اپلیکیشن‌هایی که از WebSocket استفاده می‌کنند
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```


**فعال‌سازی کانفیگ:**

```bash
# ایجاد لینک سمبلیک برای فعال شدن
sudo ln -s /etc/nginx/sites-available/my-web-app /etc/nginx/sites-enabled/

# تست صحت کانفیگ (بسیار مهم)
sudo nginx -t

# اعمال تغییرات بدون قطعی سرویس
sudo systemctl reload nginx
```

اکنون باید بتوانید اپلیکیشن را از خارج سرور با آدرس `http://app.example.com` (یا IP سرور) مشاهده کنید.

### 4. تنظیم HTTPS (بسیار توصیه‌شده)

برای امنیت بیشتر، حتماً از HTTPS استفاده کنید. ابزار `certbot` این کار را به سادگی انجام می‌دهد.

```bash
# نصب Certbot و افزونه Nginx
sudo apt install certbot python3-certbot-nginx -y

# دریافت گواهی SSL و تنظیم خودکار Nginx
sudo certbot --nginx -d app.example.com
```

Certbot به طور خودکار کانفیگ Nginx را برای ریدایرکت HTTP به HTTPS و استفاده از گواهی‌های دریافتی به‌روزرسانی می‌کند .

### 5. نکات تکمیلی و عیب‌یابی

- **بررسی لاگ‌ها:** اگر با خطا مواجه شدید، لاگ‌های Nginx را بررسی کنید: `sudo tail -f /var/log/nginx/error.log` و `sudo tail -f /var/log/nginx/access.log`.
- **تنظیم دامنه:** رکورد `A` دامنه خود را در DNS به IP عمومی سرور اشاره دهید.
- **مشکل WebSocket:** اگر اپلیکیشن شما به صورت Real-time است (مثل چت یا داشبوردهای زنده)، هدرهای `Upgrade` و `Connection` در کانفیگ بالا ضروری هستند .
- **فایل‌های استاتیک:** اگر اپلیکیشن شما دارای فایل‌های استاتیک (تصاویر، CSS) است که توسط Nginx سرو می‌شوند، می‌توانید یک بلوک `location /static/` اضافه کنید تا فشار از روی کانتینر داکر برداشته شود.