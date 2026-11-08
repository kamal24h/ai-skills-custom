به نظرم این نسخه از ارزیابی، مسیر معماری را به سطح خوبی رسانده است. اگر بخواهم صریح نظر بدهم، با تصمیم نهایی آن موافقم و پیشنهاد می‌کنم همین نسخه را مبنای توسعه قرار دهیم.

نکته مهم این است که در این مرحله دیگر اختلاف جدی معماری نداریم؛ فقط باید چند تصمیم را دقیق‌تر کنیم تا هنگام پیاده‌سازی با تناقض مواجه نشویم.

## ۱. بررسی پنج تصمیم تکمیلی

| موضوع                                       | نظر من               | تصمیم پیشنهادی                                          |
| ------------------------------------------- | -------------------- | ------------------------------------------------------- |
| محدود کردن فاز اول به یک Agent              | کاملاً موافقم        | فقط یک Use Case واقعی Inventory                         |
| ساخت Abstraction براساس نیاز واقعی          | موافقم، با یک استثنا | قرارداد مشترک Task از ابتدا لازم است؛ Registry عمومی نه |
| تقسیم فاز دوم به ۲الف و ۲ب                  | کاملاً موافقم        | ابتدا Delegation سری، سپس Parallel Execution            |
| Query Understanding به‌عنوان Pre-processing | تا حد زیادی موافقم   | اجرای شرطی و قبل از Supervisor                          |
| اضافه کردن Tenant و User به Task Contract   | کاملاً موافقم        | اجباری و غیرقابل حذف                                    |

دو نکته را بیشتر توضیح می‌دهم.

## ۲. تصمیم مهم اول: جایگاه Query Understanding

پیشنهاد من این است:

Query Understanding یک مرحله آماده‌سازی شرطی باشد، نه بخشی از چرخه تصمیم‌گیری Supervisor.

اما یک نکته وجود دارد: تشخیص اینکه درخواست ساده است یا پیچیده، خودش نیازمند تصمیم‌گیری است.

بنابراین جریان را به این شکل طراحی می‌کنم:

FastAPI Assistant API

Initial Routing / Intent Classification

تشخیص مسیر اولیه با منطق فعلی و قواعد سبک

Simple

Existing Workflow

Small Talk، RAG ساده، ERP Query ساده

Complex

Query Understanding

Supervisor

اگر Intent Classifier فعلی نتواند پیچیدگی درخواست را بدون Query Understanding تشخیص دهد، دو مرحله باید به‌صورت شرطی به هم متصل شوند؛ نه اینکه Query Understanding را برای همه درخواست‌ها اجباری کنیم.

در نتیجه، Query Understanding موجود حفظ می‌شود و جایگاه آن تغییر می‌کند، نه اینکه دوباره نوشته شود.

## ۳. تصمیم مهم دوم: Tenant و User در Task Contract

این اصلاح را ضروری می‌دانم؛ اما پیشنهاد می‌کنم اطلاعات هویتی و مجوزها را از هم تفکیک کنیم.

برای مثال:

```
class AgentTask:    task_id: str    parent_task_id: str | None    agent_type: str    objective: str    tenant_id: str    user_id: str    authorization_context: dict    input_context: dict    expected_output_schema: str    dependencies: list[str]    max_tool_calls: int    timeout_seconds: int
```

و برای نتیجه:

```
class AgentResult:    task_id: str    agent_type: str    tenant_id: str    user_id: str    status: str    result: dict    evidence: list[dict]    errors: list[dict]    execution_metrics: dict
```

اما یک اصلاح امنیتی مهم:

`authorization_context` نباید صرفاً اطلاعاتی باشد که LLM تولید می‌کند یا Agent بتواند تغییر دهد.

این اطلاعات باید از Context معتبر درخواست و لایه کنترل دسترسی سیستم تأمین شود. Agent حق ندارد با تغییر Task، سطح دسترسی خودش را افزایش دهد.

همچنین Supervisor باید قبل از هر فراخوانی MCP، اعتبار Tenant، User و مجوز مربوط به عملیات را کنترل کند. داشتن این فیلدها به‌تنهایی امنیت را تضمین نمی‌کند.

## ۴. یک اصلاح دیگر: قرارداد Task را از ابتدا طراحی کنیم، Runtime را نه

من با هشدار Over-engineering کاملاً موافقم.

به همین دلیل این تفکیک را پیشنهاد می‌کنم:

| قابلیت                    | فاز اول   |
| ------------------------- | --------- |
| Pydantic Task Contract    | لازم      |
| Pydantic AgentResult      | لازم      |
| Supervisor State          | لازم      |
| اجرای یک Inventory Agent  | لازم      |
| Delegation محدود          | لازم      |
| Agent Registry عمومی      | فعلاً خیر |
| Dynamic Agent Discovery   | خیر       |
| Distributed Agent Runtime | خیر       |
| Agent-to-Agent Messaging  | خیر       |
| حافظه مستقل هر Agent      | فعلاً خیر |
| Parallel Execution        | فاز بعد   |

این یعنی از همان ابتدا قرارداد مناسبی داریم، اما برای قابلیت‌هایی که هنوز استفاده‌کننده واقعی ندارند زیرساخت نمی‌سازیم.

## ۵. نقشه راهی که پیشنهاد می‌کنم تصویب کنیم

## نقشه راه اجرایی نهایی

1. طراحی فنی و Baseline
   - چهار سند معماری
   - دیتاست ۵۰ سؤالی
   - ثبت معیارهای فعلی
2. Phase 1 — Supervisor + Inventory
   - حفظ Workflow فعلی
   - Query Understanding شرطی
   - Task Contract
   - یک Inventory Agent
   - اجرای یک Use Case واقعی
3. Phase 2A — Sequential Delegation
   - اجرای وظایف توسط Supervisor
   - دریافت AgentResult
   - کنترل خطا و تکمیل مأموریت
   - بدون موازی‌سازی
4. Phase 2B — Parallel Execution
   - افزودن Sales Agent
   - اجرای هم‌زمان وظایف مستقل
   - کنترل Dependency
   - اندازه‌گیری زمان اجرا
5. Phase 3 — Verification & Synthesis
   - اعتبارسنجی قطعی شواهد
   - ارزیابی معنایی
   - ترکیب پاسخ نهایی
6. Phase 4 — Expansion
   - Agentهای تخصصی جدید
   - بهینه‌سازی مدل‌ها
   - حافظه و قابلیت‌های پیشرفته در صورت نیاز

## ۶. ترتیب شروع کار

من پیشنهاد می‌کنم چهار سند را دقیقاً با این ترتیب تهیه کنیم:

| اولویت | سند                          | دلیل                                   |
| ------ | ---------------------------- | -------------------------------------- |
| ۱      | Multi-Agent Architecture     | مشخص شدن مرز مسئولیت‌ها و جریان کلی    |
| ۲      | Agent Task Contract          | مشخص شدن نحوه ارتباط و تبادل اطلاعات   |
| ۳      | Supervisor & Execution State | مشخص شدن چرخه تصمیم‌گیری و اجرای وظایف |
| ۴      | Evaluation Dataset           | مشخص شدن معیار پذیرش و اندازه‌گیری     |

یک نکته: Baseline را به‌محض آماده شدن دیتاست، قبل از هر تغییر کد اجرا می‌کنیم؛ لازم نیست منتظر تکمیل همه اسناد بمانیم.

## تصمیم پیشنهادی نهایی

مبنای پیشنهادی برای تصویب

من این اصول را برای پروژه تثبیت می‌کنم:

1. معماری Hierarchical Multi-Agent با Supervisor مرکزی.
2. اجرای Selective Multi-Agent فقط برای درخواست‌های پیچیده.
3. حفظ FastAPI، LangGraph، Local RAG، Local LLM، OpenAI و ERP MCP.
4. حفظ Query Understanding به‌عنوان Pre-processing شرطی.
5. جداسازی Intent Classification، Planning و Execution.
6. Task Contract با Tenant و User اجباری.
7. شروع با یک Inventory Agent و یک Use Case واقعی.
8. ابتدا Delegation سری و بعد موازی‌سازی.
9. عدم تغییر سیاست فعلی OpenAI برای تولید پاسخ RAG.
10. ادامه توسعه فقط در صورت اثبات بهبود با معیارهای ارزیابی.

نظر نهایی من: دیگر نیازی به بحث بیشتر درباره اصل معماری نداریم. این تصمیم‌ها برای شروع طراحی فنی کافی هستند.

گام بعدی را با سند اول آغاز می‌کنیم: `Multi-Agent Architecture Specification v1.0`؛ سندی که باید دقیقاً به معماری فعلی پروژه متصل باشد و مبنای تغییرات کد قرار بگیرد.