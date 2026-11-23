

# مشخصات سخت افزار
```bach
sudo dmidecode -t system
sudo lshw -short
df -h //فضای دیسک
id // کاربر جاری و گروههای که عضو هست
```
**تعریف کاربر جاری به عنوان ادمین داکر**
```bach
sudo groupadd docker
sudo usermod -aG docker $USER
sudo chown root:docker /var/run/docker.sock

# بررسی مالکیت و مجوز فعلی فایل
ls -l /var/run/docker.sock

# اگر مالک آن root:docker نبود، آن را اصلاح کنید
sudo chown root:docker /var/run/docker.sock

# مجوزهای صحیح (خواندن و نوشتن برای مالک و گروه) را تنظیم کنید
sudo chmod 660 /var/run/docker.sock
```

# نصب ایمیج های اصلی داکر
```bach

// نصب اولاما بدون گرافیک
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
// نصب اولاما بدون گرافیک با دسترسی فقط درون داکر بدون دسترسی خارجی
docker run -d -v ollama:/root/.ollama -p 127.0.0.1:11434:11434 --name ollama ollama/ollama

// نصب اولاما روی سرور دارای گرافیک انویدیا

🔧 راه‌حل: استفاده از مخزن آینه لیارا
ابتدا باید فایل مخزن معیوب قبلی را حذف کنید و سپس مخزن جدید را با کلید GPG مربوطه اضافه کنید.

۱. حذف مخزن قبلی و پاکسازی:

bash
sudo rm -f /etc/apt/sources.list.d/docker.list
sudo apt clean
۲. دریافت کلید GPG از مخزن لیارا:

bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://linux-mirror.liara.ir/repository/ubuntu-docker/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
۳. افزودن مخزن لیارا به سیستم:

bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
Architectures: amd64
URIs: https://linux-mirror.liara.ir/repository/ubuntu-docker/
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
۴. به‌روزرسانی و نصب داکر:

bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

پس از اجرای موفق این دستورات، داکر به درستی نصب می‌شود و می‌توانید مراحل بعدی (پیکربندی NVIDIA و اجرای Ollama) را ادامه دهید. اگر در مرحله apt update با خطای جدیدی مواجه شدید، خروجی آن را ارسال کنید تا بررسی کنیم.

```
