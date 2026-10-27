

**لایه	وضعیت	نقش**
PostgreSQL	✅	منبع حقیقت
Redis	✅	cache تاریخچه
RabbitMQ	✅	صف رویداد برای fine-tuning
هر سه به درستی dual-write می‌شوند. رفتار در صورت خطا: silent skip + log warning، بدون از کار افتادن سیستم.

یادآوری برای سرویس مصرف‌کننده (consumer)
آن سرویس جداگانه‌ای که می‌خواهی برای fine-tuning بنویسی، باید:

به همان vhost / و queue LogAi وصل شود

پیام‌ها را consume کند

پس از پردازش موفق basic_ack بزند (تا از صف حذف شود)

اگر پردازش fail شد، basic_nack با requeue=True یا ارسال به DLQ (بسته به استراتژی)

اگر بخواهی، بعداً می‌توانم یک اسکلت ساده برای آن consumer هم بنویسم (مثلاً با pika یا aio-pika).





**مشاهده برخی از پیامهای صف**

docker exec -it fastapi_backend python -c "
import pika, json
from config import settings

creds = pika.PlainCredentials(settings.rabbitmq_user, settings.rabbitmq_password)
params = pika.ConnectionParameters(
    host=settings.rabbitmq_host,
    port=settings.rabbitmq_port,
    virtual_host=settings.rabbitmq_vhost,
    credentials=creds,
)
conn = pika.BlockingConnection(params)
ch = conn.channel()

method, props, body = ch.basic_get(queue=settings.rabbitmq_queue, auto_ack=False)
if method:
    print('--- message found ---')
    print(json.dumps(json.loads(body), ensure_ascii=False, indent=2))
    ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
    print('--- requeued (queue untouched) ---')
else:
    print('queue is empty')
conn.close()
"