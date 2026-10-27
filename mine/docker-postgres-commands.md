
# کامند روی دیتابیس روی داکر
docker exec -it assistant-postgres psql -U assistant_user -d assistant_db -c "
ALTER TABLE conversations
  ADD COLUMN IF NOT EXISTS user_name VARCHAR(255),
  ADD COLUMN IF NOT EXISTS tenant_desc VARCHAR(500);
"

# فیلدهای جدول خاص
docker exec -it assistant-postgres psql -U assistant_user -d assistant_db -c "\d conversations"