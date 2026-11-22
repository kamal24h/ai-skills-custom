
# کامند روی دیتابیس روی داکر
```bash
docker exec -it assistant-postgres psql -U assistant_user -d assistant_db -c "
ALTER TABLE conversations
  ADD COLUMN IF NOT EXISTS user_name VARCHAR(255),
  ADD COLUMN IF NOT EXISTS tenant_desc VARCHAR(500);
"
```

# فیلدهای جدول خاص
```bash
docker exec -it assistant-postgres psql -U assistant_user -d assistant_db -c "\d conversations"
```

**بررسی ساختار جدول**

```bash
docker compose exec postgres psql -U assistant_user -d assistant_db -c "\d conversations"
```

**کوئری روی جدول**

```bash
docker compose exec postgres psql -U assistant_user -d assistant_db -c "ALTER TABLE conversations ADD COLUMN tools_id_list TEXT[] DEFAULT '{}';"
```

**افزودن مایگریشن با المبیک**

```bash
docker compose exec rag alembic revision --autogenerate -m "add tools_id_list to conversations"
```