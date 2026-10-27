# معماری نهایی سامانه تحلیل داده مبتنی بر LLM

با توجه به انتخاب‌های تو، پیشنهاد من معماری Hybrid LLM Analytics Assistant است: یک سامانه تحلیل داده با Python که از LangGraph برای مدیریت گردش کار، از LangChain برای اتصال مدل و ابزارها، از دیتابیس رابطه‌ای برای داده‌های اصلی و از ترکیب LLM محلی و ابری برای تحلیل و استدلال استفاده می‌کند.

در این معماری، سه اصل طراحی داریم:

1. داده و محاسبات، مرجع حقیقت هستند؛ نه LLM. مدل کوئری را پیشنهاد می‌دهد و نتایج را تفسیر می‌کند؛ SQL و ابزارهای آماری محاسبات واقعی را انجام می‌دهند.
2. LangGraph کنترل‌کننده گردش کار است. تصمیم می‌گیرد چه ابزاری اجرا شود، نتیجه چگونه اعتبارسنجی شود و چه زمانی به مدل ابری نیاز است.
3. مدل محلی مسیر پیش‌فرض است؛ مدل ابری مسیر اختیاری برای استدلال دشوار. اطلاعات حساس و داده خام تا حد امکان در محیط داخلی باقی می‌مانند.

این طرح برای یک دستیار تحلیلی سازمانی مناسب است که به سؤال‌های کاربران درباره فروش، موجودی، عملکرد، روندها، شاخص‌های کلیدی و تحلیل آماری پاسخ می‌دهد.

## ۱. نمودار معماری کلان

Analytics User / Client

سؤال طبیعی، فیلترها، درخواست گزارش و نمودار

FastAPI — Application API

Authentication، Pydantic Validation، Session، Streaming

## LangGraph Orchestrator

Intent & Planner

تشخیص هدف و طراحی تحلیل

Schema Context

ساختار داده و تعاریف کسب‌وکار

Policy & SQL Validation

مجوز، کنترل و اعتبارسنجی

Execute & Evaluate

اجرا، ارزیابی و اصلاح محدود

Local LLM

Ollama یا vLLM

طبقه‌بندی، تولید SQL اولیه، استخراج ساخت‌یافته و تفسیر عادی

Cloud LLM API

مدل استدلالی خارجی

حل مسائل پیچیده، تحلیل چندمرحله‌ای و موارد دشوار

SQL Analytics Tools

SQLAlchemy + SQL Database

بازیابی داده، گروه‌بندی و تجمیع

Statistics Engine

Pandas / Polars / SciPy

روند، همبستگی، آزمون آماری و پیش‌بینی

Result & Visualization Layer

جدول، شاخص، داده نمودار، شواهد و متادیتای نتیجه

Answer Synthesizer

پاسخ فارسی، توضیح روند، منبع داده و محدودیت تحلیل

نکته مهم: Local LLM، Cloud LLM، دیتابیس و موتور آمار، ابزارها و سرویس‌های جداگانه‌اند؛ LangGraph مسیر فراخوانی و کنترل بین آن‌ها را مدیریت می‌کند. این تفکیک، امکان تغییر مدل یا موتور محاسباتی را بدون بازنویسی کل سیستم فراهم می‌کند.

## ۲. ساختار دقیق LangGraph

پیشنهاد می‌کنم در نسخه اول، به‌جای چند Agent مستقل، از یک Graph مرکزی با Nodeهای مشخص و Toolهای تخصصی استفاده کنی. این الگو امکان ترکیب مراحل قطعی با تصمیم‌گیری LLM را می‌دهد و با قابلیت‌های اصلی LangGraph برای وضعیت پایدار، ادامه اجرا و کنترل انسانی هم‌خوان است.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://langchain-ai.github.io\&sz=32)

Docs by LangChain

+1



\#chatgpt-mermaid-\_r_qf\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_qf\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_qf\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_qf\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_qf\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_qf\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_qf\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_qf\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_qf\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_qf\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_qf\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_qf\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_qf\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_qf\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_qf\_ p{margin:0;}#chatgpt-mermaid-\_r_qf\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_qf\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_qf\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_qf\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_qf\_ .label text,#chatgpt-mermaid-\_r_qf\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_qf\_ .node rect,#chatgpt-mermaid-\_r_qf\_ .node circle,#chatgpt-mermaid-\_r_qf\_ .node ellipse,#chatgpt-mermaid-\_r_qf\_ .node polygon,#chatgpt-mermaid-\_r_qf\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_qf\_ .rough-node .label text,#chatgpt-mermaid-\_r_qf\_ .node .label text,#chatgpt-mermaid-\_r_qf\_ .image-shape .label,#chatgpt-mermaid-\_r_qf\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_qf\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_qf\_ .rough-node .label,#chatgpt-mermaid-\_r_qf\_ .node .label,#chatgpt-mermaid-\_r_qf\_ .image-shape .label,#chatgpt-mermaid-\_r_qf\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_qf\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_qf\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_qf\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_qf\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_qf\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_qf\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_qf\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_qf\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_qf\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_qf\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_qf\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_qf\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_qf\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_qf\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_qf\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_qf\_ .icon-shape,#chatgpt-mermaid-\_r_qf\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_qf\_ .icon-shape p,#chatgpt-mermaid-\_r_qf\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_qf\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_qf\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_qf\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_qf\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_qf\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_qf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_qf\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_qf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_qf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_qf\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_qf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_qf\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_qf\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_qf\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_qf\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_qf\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_qf\_ .node rect,#chatgpt-mermaid-\_r_qf\_ .node circle,#chatgpt-mermaid-\_r_qf\_ .node ellipse,#chatgpt-mermaid-\_r_qf\_ .node polygon,#chatgpt-mermaid-\_r_qf\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_qf\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_qf\_ .node.mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_qf\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_qf\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_qf\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}START: User QuestionLoad Context and PermissionsClassify Intent - Local LLMLoad Relevant SchemaBuild Analysis PlanAnalysis TypeGenerate SQLPlan Statistical WorkflowPlan SQL + StatisticsSQL Policy ValidatorExecute Read-only QueryValidate ResultRun Statistical ToolsEnough Data and Valid?Bounded Retry or ClarificationBuild Result Summary andChart SpecComplex Reasoning Needed?Local LLM: AnswerPolicy Check and ContextMinimizationCloud LLM: AdvancedReasoningValidate Cloud OutputFormat ResponseEND: Answer + Tables +EvidenceBusiness ReportStatistical AnalysisCombinedNoYesNoYes

### منطق تصمیم‌گیری

| وضعیت درخواست                                              | مسیر پیشنهادی                    |
| ---------------------------------------------------------- | -------------------------------- |
| «فروش این ماه چقدر است؟»                                   | SQL + Local LLM                  |
| «فروش هر ماه را با ماه قبل مقایسه کن»                      | SQL + محاسبات آماری              |
| «روند فروش چه بوده و چه عواملی ممکن است آن را توضیح دهند؟» | SQL + آمار + احتمالاً Cloud LLM  |
| «آیا تفاوت فروش دو گروه از نظر آماری معنادار است؟»         | SQL + SciPy یا ابزار آماری معتبر |
| درخواست مبهم یا فاقد اطلاعات کافی                          | سؤال تکمیلی، نه حدس‌زدن          |

تصمیم استفاده از مدل ابری باید در یک Node یا Policy مشخص انجام شود؛ نه اینکه مدل محلی بتواند بدون محدودیت هر داده‌ای را به سرویس خارجی ارسال کند.

## ۳. تقسیم وظایف بین Local LLM و Cloud LLM

Local LLM — مسیر پیش‌فرض

- تشخیص Intent و نوع گزارش
- انتخاب ابزار و تولید اولیه SQL
- تبدیل سؤال به پارامترهای ساخت‌یافته
- توضیح نتایج متعارف و پاسخ فارسی
- کار در شرایط قطع اینترنت، مشروط به آماده‌بودن سرویس و مدل محلی

Cloud LLM — مسیر استدلال پیشرفته

- تحلیل چندمرحله‌ای با چند شاخص و محدودیت
- تفسیر الگوهای پیچیده با زمینه کسب‌وکار
- بررسی فرضیه‌ها و پیشنهاد تحلیل‌های تکمیلی
- کمک به توضیح نتایج آماری، بدون جایگزینی محاسبات معتبر

برای اجرای مدل محلی، Ollama شروع ساده‌ای است؛ اگر بعداً به سرویس‌دهی هم‌زمان بیشتر و کنترل دقیق‌تر استقرار نیاز داشتی، vLLM را ارزیابی کن. Ollama از Tool Calling و خروجی ساخت‌یافته پشتیبانی می‌کند؛ این قابلیت‌ها برای تولید Intent و پارامترهای معتبر مفیدند.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub

+1



یک نکته مهم: اگر GPU محدود باشد، مدل محلی را برای وظایف ساده و کوتاه به‌کار بگیر و برای وظایف پیچیده از Cloud استفاده کن. انتخاب مدل نهایی باید با توجه به زبان فارسی، کیفیت تولید SQL، Tool Calling و سخت‌افزار واقعی تست شود.

## ۴. ابزارهای تحلیلی که باید بسازی

این Toolها بهتر است توابع Python مشخص با ورودی و خروجی تعریف‌شده باشند، نه ابزارهایی که اجازه اجرای آزاد هر کد یا کوئری را می‌دهند.

| ابزار                     | مسئولیت                               |
| ------------------------- | ------------------------------------- |
| `get_schema_context`      | ارائه Schema و توضیحات جداول مجاز     |
| `get_business_metrics`    | ارائه تعریف رسمی شاخص‌ها              |
| `generate_sql`            | تولید SQL با مدل محلی                 |
| `validate_sql`            | کنترل ساختار، جداول مجاز و محدودیت‌ها |
| `execute_readonly_sql`    | اجرای کوئری مجاز با محدودیت منابع     |
| `aggregate_data`          | گروه‌بندی، تجمیع و محاسبات جدولی      |
| `calculate_kpis`          | محاسبه شاخص‌هایی مثل رشد و میانگین    |
| `run_statistical_test`    | آزمون‌های آماری معتبر                 |
| `forecast_series`         | پیش‌بینی سری زمانی در صورت نیاز       |
| `build_chart_spec`        | تولید مشخصات ساخت‌یافته نمودار        |
| `request_cloud_reasoning` | ارسال زمینه پالایش‌شده به مدل ابری    |
| `validate_final_answer`   | کنترل تطابق پاسخ با نتایج واقعی       |

برای SQL می‌توان از SQLAlchemy و برخی الگوهای LangChain استفاده کرد؛ اما نباید یک SQL Agent با دسترسی آزاد به دیتابیس را مستقیماً در محیط Production قرار داد. مستندات LangChain نیز درباره خطر اجرای SQL تولیدشده توسط مدل و لزوم دسترسی حداقلی، محدودیت منابع و پایش هشدار می‌دهند.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://reference.langchain.com\&sz=32)

LangChain Reference

+1



### نکته درباره تحلیل آماری

محاسبات را تا حد امکان از LLM جدا نگه دار:

- رشد درصدی، میانگین و انحراف معیار: NumPy یا Pandas
- آزمون فرض و همبستگی: SciPy
- پیش‌بینی: ابتدا مدل‌های آماری و سری زمانی متناسب با داده
- یادگیری ماشین: scikit-learn در صورت وجود نیاز واقعی

مثلاً اگر مدل ادعا کند فروش ۱۸ درصد رشد کرده، این عدد باید از خروجی محاسباتی قابل بازتولید آمده باشد، نه از متن تولیدشده توسط مدل.

## ۵. ساختار پیشنهادی پروژه Python

برای اینکه پروژه بعداً قابل نگهداری و توسعه باشد، منطق API، گراف، ابزارهای داده، اتصال مدل‌ها و لایه دیتابیس را جدا نگه دار.

```

analytics-assistant/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── analytics.py
│   │       └── sessions.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── policies.py
│   ├── schemas/
│   │   ├── requests.py
│   │   ├── responses.py
│   │   ├── analytics.py
│   │   └── charts.py
│   ├── graph/
│   │   ├── state.py
│   │   ├── builder.py
│   │   ├── routing.py
│   │   └── nodes/
│   │       ├── classify.py
│   │       ├── planning.py
│   │       ├── sql_generation.py
│   │       ├── validation.py
│   │       ├── execution.py
│   │       ├── statistics.py
│   │       └── synthesis.py
│   ├── llm/
│   │   ├── local.py
│   │   ├── cloud.py
│   │   └── router.py
│   ├── tools/
│   │   ├── schema_tools.py
│   │   ├── sql_tools.py
│   │   ├── statistics_tools.py
│   │   └── visualization_tools.py
│   ├── data/
│   │   ├── database.py
│   │   ├── schema_catalog.py
│   │   └── query_executor.py
│   ├── services/
│   │   ├── analytics_service.py
│   │   ├── session_service.py
│   │   └── result_service.py
│   └── persistence/
│       ├── checkpoints.py
│       └── repositories.py
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── security/
│   └── evaluation/
├── prompts/
├── migrations/
├── Dockerfile
├── compose.yaml
├── pyproject.toml
└── .env.example

```

این ساختار پیشنهادی است، نه الزام LangChain. برای MVP می‌توانی بعضی پوشه‌ها را ادغام کنی؛ مهم این است که منطق تحلیل مستقیماً داخل Endpointهای FastAPI قرار نگیرد.

## ۶. اجزای اجرایی و استقرار

برای نسخه اولیه، استقرار با Docker Compose روی یک سرور Linux انتخاب مناسبی است.

## سرویس‌های اصلی

analytics-api

FastAPI + Uvicorn

ورودی HTTP، اعتبارسنجی و مدیریت درخواست

local-llm

Ollama یا vLLM

سرویس مدل زبانی محلی

postgres

PostgreSQL

تاریخچه، متادیتا و Checkpoint در صورت انتخاب این Backend

redis

Redis، اختیاری

کش، محدودیت نرخ و هماهنگی کارهای موقت

analytics-db

دیتابیس رابطه‌ای موجود

داده‌های اصلی، با دسترسی فقط‌خواندنی و محدود

Cloud LLM یک سرویس خارجی است و لزوماً Container جداگانه‌ای در شبکه تو نخواهد داشت. همچنین اگر دیتابیس اصلی از قبل در محیط دیگری اجرا می‌شود، نیازی به راه‌اندازی مجدد آن در Compose نیست.

### وابستگی‌های Python

برای شروع، این مجموعه مناسب است:

```
fastapi
uvicorn[standard]
pydantic
pydantic-settings

langchain
langchain-core
langgraph
langchain-ollama
langchain-openai

sqlalchemy
psycopg[binary]
pandas
numpy
scipy

psycopg-pool
langgraph-checkpoint-postgres
redis
```

نکات اجرایی:

- `psycopg` فقط در صورت استفاده از PostgreSQL به‌عنوان دیتابیس کاربردی یا Checkpoint مناسب است؛ برای SQL Server از درایور سازگار با SQL Server استفاده کن.
- `langchain-openai` برای سرویس‌های سازگار با API مربوطه است؛ ارائه‌دهنده ابری را بر اساس نیاز انتخاب کن.
- اگر Redis در نسخه اول لازم نیست، حذفش کن.
- نسخه دقیق پکیج‌ها را قفل و در CI تست کن؛ سازگاری نسخه‌های LangChain و LangGraph را پیش از انتشار بررسی کن.

برای Checkpoint پایدار، PostgreSQL گزینه مناسبی است. Checkpointer وضعیت گراف را برای ادامه مکالمه و بازیابی اجرا حفظ می‌کند؛ آن را با تاریخچه کسب‌وکار یا حافظه دائمی کاربر یکی ندان.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub

+1



## ۷. APIهای اصلی

| Endpoint                              | کاربرد                          |
| ------------------------------------- | ------------------------------- |
| `POST /api/v1/analytics/query`        | ارسال سؤال و دریافت پاسخ تحلیلی |
| `POST /api/v1/analytics/query/stream` | دریافت تدریجی وضعیت و پاسخ      |
| `GET /api/v1/analytics/sessions/{id}` | دریافت وضعیت یا تاریخچه نشست    |
| `GET /api/v1/analytics/results/{id}`  | دریافت نتیجه ذخیره‌شده یک تحلیل |
| `GET /health/live`                    | بررسی زنده‌بودن سرویس           |
| `GET /health/ready`                   | بررسی آمادگی وابستگی‌های ضروری  |

در پاسخ تحلیلی، علاوه بر متن، فیلدهای ساخت‌یافته‌ای مثل `summary`، `tables`، `chart_spec`، `data_period`، `sources` و `warnings` برگردان. در این صورت Frontend برای نمایش جدول و نمودار به استخراج اطلاعات از متن آزاد LLM وابسته نمی‌شود.

## ۸. ملاحظات ضروری Production

پیش از اتصال کاربران واقعی، این موارد را جزو الزامات طراحی قرار بده:

- مجوز داده: محدودیت دسترسی کاربر باید در سمت سرور و دیتابیس اعمال شود، نه فقط در Prompt.
- کنترل SQL: محدودکردن Schema و عملیات، Read-only، محدودیت زمان اجرا، تعداد ردیف‌ها و هزینه کوئری.
- محرمانگی مدل ابری: ارسال حداقل داده لازم؛ حذف اطلاعات شناسایی‌کننده و اطلاعات حساس پیش از فراخوانی API خارجی.
- کنترل حلقه‌ها: تعداد Retry و تعداد Tool Call در هر درخواست محدود باشد.
- پایداری: Timeout، مدیریت خطا، لغو درخواست و بازیابی وضعیت اجرا.
- مشاهده‌پذیری: ثبت زمان هر Node، مدل انتخاب‌شده، تعداد توکن‌ها، هزینه، خطاها و شناسه درخواست؛ از ثبت غیرضروری داده حساس خودداری کن.
- ارزیابی: تست مجموعه‌ای از سؤالات واقعی با SQL و نتیجه مورد انتظار، شامل سؤالات مبهم، کوئری‌های نامعتبر و درخواست‌های خارج از مجوز.

## ۹. برنامه اجرایی پیشنهادی

1. فاز اول — گزارش‌گیری پایه: اتصال Read-only به دیتابیس، Schema Catalog، تولید و اعتبارسنجی SQL، اجرای کوئری و پاسخ فارسی با مدل محلی.
2. فاز دوم — تحلیل آماری: افزودن محاسبات Pandas/SciPy، شاخص‌های تعریف‌شده، مقایسه دوره‌ای و خروجی نمودار.
3. فاز سوم — مسیریابی Hybrid: افزودن Policy برای انتخاب مدل محلی یا ابری، پالایش زمینه ارسالی و مدیریت خطاهای سرویس خارجی.
4. فاز چهارم — Production: Checkpoint پایدار، مدیریت نشست‌ها، محدودیت منابع، ارزیابی خودکار، مانیتورینگ و تست امنیتی.

### جمع‌بندی نهایی

برای این پروژه، معماری مناسب عبارت است از FastAPI + LangGraph به‌عنوان Orchestrator + LangChain برای اتصال مدل‌ها و ابزارها + SQLAlchemy برای دسترسی کنترل‌شده به دیتابیس + Pandas/SciPy برای تحلیل آماری + Local/Cloud LLM Router.

از ابتدا Multi-Agent پیچیده نساز. یک Graph مرکزی با مسیرهای روشن و Toolهای مستقل ایجاد کن. ابتدا صحت SQL و محاسبات را قابل اعتماد کن، سپس استدلال ابری و قابلیت‌های پیشرفته را اضافه کن. این ترتیب ریسک فنی را کم می‌کند و ارزیابی کیفیت را بسیار ساده‌تر می‌سازد.