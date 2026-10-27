
**ساختن فایل جدید**
touch /opt/assistant/config.txt
touch filename

**بازکردن ویرایشگر فایل**
nano /opt/assistant/config.txt
vim /opt/assistant/config.txt

**و یا با ویرایشگر گرافیکی**
gedit /opt/assistant/config.txt


**نوشتن سریع محتوا**
cat > file.txt << 'EOF' ... EOF

**افزودن به فایل**
echo "text" >> file.txt


**ساخت پوشه**

sudo mkdir -p directory (/opt/assistant)

**چک کردن ساخت پوشه:**
ls -ld directory (/opt/assistant)

**مالکیت پوشه را به کاربر خودتان بدهید (تا بدون ادمین یا سودو بتوانید در آن**
**کار کنید)، می‌توانید دستور زیر را اجرا کنید:**
bash
sudo chown -R $USER:$USER directory (/opt/assistant)

**رفتن به پوشه**
cd directory (/opt/assistant)

**حذف پوشه پر و فایلهای زیرمجموعه**
rm -r /opt/assistant

**حذف پوشه خالی**
rmdir -p directory

**حذف با تأیید گرفتن برای هر فایل (امن‌تر)**
rm -ri /opt/assistant

**روش امن حذف همه فایل ها در پوشه جاری**
cd /مسیر/دقیق/پوشه
pwd   # تأیید مسیر
ls -la   # مشاهده محتویات
rm -rf ./* ./.[!.]* 2>/dev/null