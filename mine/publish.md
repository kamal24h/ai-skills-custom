برای دسترسی به دستیار هوشمند از خارج از سرور، باید چند لایه کار انجام دهید: **پیکربندی شبکه و دامنه**، **راه‌اندازی Nginx به عنوان Reverse Proxy**، **دریافت SSL/HTTPS**، و **مقاوم‌سازی امنیتی سرور**.

در ادامه مراحل را قدم‌به‌قدم توضیح می‌دهم.

### 📌 گام صفر: پیش‌نیازها

1. **دامنه (Domain):** یک دامنه یا ساب‌دامین ثبت شده داشته باشید (مثلاً `assistant.example.com`).
2. **رکورد DNS:** در پنل مدیریت دامنه، یک **رکورد A** ایجاد کنید که به IP عمومی سرور شما اشاره کند .
3. **دسترسی SSH:** مطمئن شوید SSH روی سرور فعال است و می‌توانید با کلید SSH وارد شوید .

### 🔥 گام اول: پیکربندی فایروال (UFW)

قبل از هر چیز، باید پورت‌های لازم را در فایروال سرور باز کنید. **مهم:** ابتدا پورت SSH را باز کنید، سپس فایروال را فعال کنید، در غیر این صورت دسترسی خود را از دست می‌دهید.

```bash
# اجازه SSH (پورت 22 یا پورت سفارشی خودتان)
sudo ufw allow 22/tcp

# اجازه HTTP و HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# فعال‌سازی فایروال
sudo ufw enable

# بررسی وضعیت
sudo ufw status verbose
```

**نکته مهم:** پورت `8000` (FastAPI) را **باز نکنید**. این پورت باید فقط از داخل سرور (لوکال) در دسترس باشد و ترافیک از طریق Nginx به آن هدایت شود .

### 🌐 گام دوم: نصب و پیکربندی Nginx به عنوان Reverse Proxy

Nginx به عنوان یک واسط بین اینترنت و FastAPI شما عمل می‌کند. درخواست‌های HTTPS را دریافت کرده و به سرویس پایتون شما روی پورت `8000` (یا هر پورت دیگری) هدایت می‌کند .

**۱. نصب Nginx:**
```bash
sudo apt update
sudo apt install nginx -y
```

**۲. ایجاد فایل پیکربندی برای سایت خود:**
```bash
sudo nano /etc/nginx/sites-available/assistant.example.com.conf
```

**۳. محتوای فایل کانفیگ (نسخه اولیه HTTP):**
```nginx
server {
    listen 80;
    listen [::]:80;

    server_name assistant.example.com;

    location / {
        proxy_pass         http://127.0.0.1:8000;
        proxy_http_version 1.1;

        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;

        # برای پشتیبانی از Streaming و WebSocket
        proxy_set_header   Upgrade           $http_upgrade;
        proxy_set_header   Connection        "upgrade";
    }
}
```

**۴. فعال‌سازی سایت و بارگذاری مجدد Nginx:**
```bash
sudo ln -s /etc/nginx/sites-available/assistant.example.com.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

حالا باید بتوانید دستیار خود را از خارج از سرور با آدرس `http://assistant.example.com` (به جای `127.0.0.1:8000`) فراخوانی کنید.

### 🔒 گام سوم: دریافت SSL رایگان با Certbot (HTTPS)

استفاده از HTTP امن نیست و داده‌های شما را در معرض خطر قرار می‌دهد. با استفاده از Certbot و Let's Encrypt می‌توانید یک گواهی SSL رایگان دریافت کنید .

```bash
# نصب Certbot و پلاگین Nginx
sudo apt install certbot python3-certbot-nginx -y

# دریافت و نصب خودکار گواهی
sudo certbot --nginx -d assistant.example.com
```

Certbot از شما ایمیل می‌خواهد و شرایط استفاده را تأیید می‌کند. سپس به طور خودکار فایل کانفیگ Nginx شما را ویرایش می‌کند و HTTPS را فعال می‌کند. همچنین تمام ترافیک HTTP را به HTTPS ریدایرکت می‌کند .

**بررسی تمدید خودکار:**
```bash
sudo certbot renew --dry-run
```

### 🛡️ گام چهارم: مقاوم‌سازی امنیتی سرور (بسیار مهم)

از آنجایی که سرور شما در معرض اینترنت عمومی قرار می‌گیرد، باید اقدامات امنیتی را انجام دهید تا از حملات خودکار ربات‌ها در امان باشید .

**۱. غیرفعال کردن لاگین با پسورد (فقط SSH Key):**
```bash
sudo nano /etc/ssh/sshd_config
```
این مقادیر را تنظیم کنید:
```
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```
سپس:
```bash
sudo systemctl restart ssh
```
**هشدار:** قبل از بستن سشن فعلی، در یک ترمینال دیگر تست کنید که با کلید SSH می‌توانید وارد شوید.

**۲. نصب و پیکربندی Fail2Ban:**
این ابزار به طور خودکار IPهایی که تلاش‌های ناموفق مکرر برای اتصال دارند را بلاک می‌کند .
```bash
sudo apt install fail2ban -y
sudo systemctl enable --now fail2ban
```

### ⚙️ گام پنجم: اجرای FastAPI به صورت Daemon (Systemd)

در حال حاضر FastAPI شما با `uvicorn` دستی اجرا می‌شود. برای اینکه در صورت قطع شدن ترمینال یا ری‌استارت سرور، سرویس شما به کار خود ادامه دهد، باید آن را به یک سرویس Systemd تبدیل کنید .

**۱. ایجاد فایل سرویس:**
```bash
sudo nano /etc/systemd/system/assistant.service
```

**۲. محتوای فایل:**
```ini
[Unit]
Description=Hybrid Assistant FastAPI Service
After=network.target

[Service]
User=arisa
Group=arisa
WorkingDirectory=/opt/assistant
Environment="PATH=/opt/assistant/venv/bin"
ExecStart=/opt/assistant/venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```
*(مسیرها و نام کاربری را با سرور خود تطبیق دهید)*

**۳. فعال‌سازی و اجرا:**
```bash
sudo systemctl daemon-reload
sudo systemctl start assistant
sudo systemctl enable assistant
```

### 🚀 نتیجه نهایی

پس از طی این مراحل، دستیار هوشمند شما با آدرس `https://assistant.example.com` از هر نقطه‌ای در دنیا قابل دسترسی خواهد بود، ارتباط آن رمزنگاری شده و سرور شما در برابر حملات رایج مقاوم‌سازی شده است.

### 💡 نکات تکمیلی

- **احراز هویت API:** چون دستیار شما به اینترنت باز است، حتماً یک لایه احراز هویت (مثل API Key یا JWT) به FastAPI اضافه کنید تا فقط کاربران مجاز بتوانند از آن استفاده کنند .
- **مدیریت حجم درخواست:** در فایل کانفیگ Nginx، در صورت نیاز می‌توانید `client_max_body_size` را تنظیم کنید تا امکان آپلود فایل‌های بزرگ‌تر برای Embedding فراهم شود .