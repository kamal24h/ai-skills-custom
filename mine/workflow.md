برای پیاده‌سازی این سیستم هایبرید سازمانی، معماری مبتنی بر **StateGraph** در **LangGraph** همراه با یک **Supervisor/Router Agent** و جداسازی تخصصی وظایف میان گره‌ها (Nodes) بهترین بازدهی، امنیت و کنترل‌پذیری را فراهم می‌کند.

در این معماری:

1. **Local RAG Node:** پرسش‌های دانشی و مستندات را با استفاده از وکتور دیتابیس لوکال (مانند Qdrant) و مدل لوکال بازخوانی می‌کند.
2. **ERP Assistant Node:** عملیات دیتابیسی، گزارش‌گیری و تراکنش‌ها را از طریق ابزارها (Tools / MCP Server یا APIهای ASP.NET Core) مدیریت می‌کند.
3. **External Fallback/Complex Node:** پرسش‌های چندمرحله‌ای، استدلال‌های سنگین و ترجمه/خلاصه‌سازی پیچیده را به مدل‌های ابری هدایت می‌کند.
4. **Guardrail & Security:** قبل از هر تماس خارجی یا عملیات تغییر داده در ERP، داده‌های حساس ماسک شده یا تأیید انسانی (Human-in-the-Loop) اعمال می‌شود.

---

### ۱. معماری کلی وضعیت (State Definition)

ابتدا ساختار داده‌ای مشترک بین تمام گره‌های گراف را تعریف می‌کنیم:

```python
from typing import Annotated, Sequence, TypedDict, Literal, Optional
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    intent: Optional[Literal["rag", "erp", "external", "direct_chat"]]
    is_complex: bool
    requires_approval: bool
    intermediate_data: Optional[dict]
    final_response: Optional[str]

```

---

### ۲. طراحی گره‌ها (Nodes)

#### الف) گره مسیریاب هوشمند (Supervisor / Intent Classifier)

این گره با یک مدل لوکال سریع (مثل `Qwen-2.5-7B` یا `Llama-3.1-8B`) تصمیم می‌گیرد کاربر چه قصدی دارد و آیا موضوع نیاز به استدلال سنگین دارد یا خیر:

```python
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

class RoutingDecision(BaseModel):
    intent: Literal["rag", "erp", "external", "direct_chat"] = Field(
        description="دسته بندی قصد کاربر: rag برای مستندات، erp برای عملیات سیستم، external برای استدلال های بسیار پیچیده یا تحلیلی، direct_chat برای احوالپرسی"
    )
    is_complex: bool = Field(description="آیا مسئله نیازمند مدل قویتر خارجی است؟")

def supervisor_node(state: AgentState):
    prompt = ChatPromptTemplate.from_messages([
        ("system", """شما تحلیل‌گر درخواست سازمانی هستید. 
        قصد کاربر را طبق ورودی تعیین کنید:
        - rag: پرسش از آیین‌نامه‌ها، مستندات، راهنماها و PDFهای داخلی
        - erp: استعلام انبار، فاکتور، وضعیت پرسنلی، صدور سند یا هر نوع عملیات روی پایگاه داده و APIهای ERP
        - external: تحلیل‌های عمیق استراتژیک، کدنویسی پیشرفته یا خلاصه‌سازی‌های عظیم
        - direct_chat: گفتگوهای عمومی و احوالپرسی"""),
        ("placeholder", "{messages}")
    ])
    
    # استفاده از Local LLM با ساختار خروجی مقید (Structured Output)
    structured_llm = local_llm.with_structured_output(RoutingDecision)
    chain = prompt | structured_llm
    decision = chain.invoke({"messages": state["messages"]})
    
    return {
        "intent": decision.intent,
        "is_complex": decision.is_complex
    }

```

#### ب) گره جستجوی مستندات داخلی (Local RAG)

این بخش به رتریور محلی (Dense + Reranker) متصل است و محتوای مستندات را برای پاسخ‌گویی استخراج می‌کند:

```python
from langchain_core.prompts import PromptTemplate

def local_rag_node(state: AgentState):
    query = state["messages"][-1].content
    
    # بازیابی اسناد از Qdrant / چانک‌های سازمان
    retrieved_docs = vector_retriever.invoke(query)
    context_str = "\n\n".join([doc.page_content for doc in retrieved_docs])
    
    prompt = PromptTemplate.from_template("""بر اساس مستندات داخلی سازمان به پرسش زیر پاسخ دقیق و مستند بده:
    مستندات:
    {context}
    
    پرسش: {query}
    پاسخ:""")
    
    chain = prompt | local_llm
    response = chain.invoke({"context": context_str, "query": query})
    
    return {"messages": [response]}

```

#### ج) گره دستیار ERP (Tool-Calling Agent)

این گره وظیفه فراخوانی توابع یا اندپوینت‌های سیستم ERP را دارد. اگر درخواست شامل تغییر داده (Create/Update/Delete) باشد، وضعیت به مرحله تایید کاربر می‌رود:

```python
from langgraph.prebuilt import ToolNode

# تعریف ابزارهای ارتباط با ERP (مثل استعلام موجودی یا ثبت سفارش)
erp_tools = [get_inventory_status, query_invoices, register_purchase_request]

def erp_assistant_node(state: AgentState):
    llm_with_tools = local_llm.bind_tools(erp_tools)
    response = llm_with_tools.invoke(state["messages"])
    
    # بررسی آیا ابزار فراخوانی شده نیاز به تایید مالی/مدیریتی دارد
    requires_approval = False
    if response.tool_calls:
        for tool_call in response.tool_calls:
            if tool_call["name"] in ["register_purchase_request", "update_ledger"]:
                requires_approval = True
                
    return {
        "messages": [response],
        "requires_approval": requires_approval
    }

```

#### د) گره هوش مصنوعی خارجی (External AI API)

برای استدلال‌های پیچیده یا داده‌های حجیم که مدل لوکال توانایی پردازش کافی را ندارد، ابتدا اطلاعات حساس (PII / محرمانگی تجاری) در قالب Guardrail فیلتر شده و سپس به API خارجی ارسال می‌شود:

```python
def external_ai_node(state: AgentState):
    # مرحله ۱: ماسک‌کردن داده‌های حساس (Sanitization)
    sanitized_messages = sanitize_pii(state["messages"])
    
    # مرحله ۲: ارسال به مدل ابری قدرتمند
    response = external_cloud_llm.invoke(sanitized_messages)
    
    return {"messages": [response]}

```

---

### ۳. ساختار و سیم‌کشی گراف (StateGraph Wiring)

```python
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver

builder = StateGraph(AgentState)

# افزودن گره‌ها
builder.add_node("supervisor", supervisor_node)
builder.add_node("local_rag", local_rag_node)
builder.add_node("erp_assistant", erp_assistant_node)
builder.add_node("erp_tools", ToolNode(erp_tools))
builder.add_node("external_ai", external_ai_node)

# لبه‌های شرطی بر اساس تصمیم Supervisor
def route_next(state: AgentState) -> str:
    if state["is_complex"]:
        return "external_ai"
    if state["intent"] == "rag":
        return "local_rag"
    elif state["intent"] == "erp":
        return "erp_assistant"
    elif state["intent"] == "external":
        return "external_ai"
    return END

builder.add_edge(START, "supervisor")
builder.add_conditional_edges("supervisor", route_next, {
    "local_rag": "local_rag",
    "erp_assistant": "erp_assistant",
    "external_ai": "external_ai",
    END: END
})

# بررسی حلقه ابزار در ERP
def erp_post_check(state: AgentState) -> str:
    last_msg = state["messages"][-1]
    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
        return "erp_tools"
    return END

builder.add_conditional_edges("erp_assistant", erp_post_check, {
    "erp_tools": "erp_tools",
    END: END
})
builder.add_edge("erp_tools", "erp_assistant")

builder.add_edge("local_rag", END)
builder.add_edge("external_ai", END)

# کامپایل همراه با Memory Checkpointer و امکان وقفه انسانی (HITL)
checkpointer = MemorySaver()
app = builder.compile(
    checkpointer=checkpointer,
    interrupt_before=["erp_tools"] if True else [] # در صورت نیاز به وقفه پیش از اجرای اکشن‌های حساس ERP
)

```

---

### ۴. نمودار جریان اجرای درخواست‌ها

```text
               +-------------------+
               |    کاربر ورودی    |
               +---------+---------+
                         |
                         v
               +---------+---------+
               | Supervisor/Router |
               +---------+---------+
                         |
       +-----------------+-----------------+
       |                 |                 |
(قصد اسناد)       (قصد سیستم)       (استدلال سنگین/پیچیده)
       v                 v                 v
+-------------+   +--------------+   +---------------+
|  Local RAG  |   | ERP Assistant|   |  External API |
|   (Qdrant)  |   | (Tool-Calling|   | (Sanitized PII|
+------+------+   +-------+------+   +-------+-------+
       |                  |                  |
       |           [Tool Call?]              |
       |          /            \             |
       |       (خیر)           (بله)          |
       |        |                |           |
       |        |          +-----+-----+     |
       |        |          | HITL Check|     |
       |        |          |  (تأیید)   |     |
       |        |          +-----+-----+     |
       |        |                |           |
       |        |          +-----+-----+     |
       |        |          | ERP Tools |     |
       |        |          +-----+-----+     |
       |        |                |           |
       |        +<---------------+           |
       |        |                            |
       +------->+--------------------------->+
                         |
                         v
               +---------+---------+
               |  پاسخ نهایی کاربر |
               +-------------------+

```

---

### ۵. نکات کلیدی برای پیاده‌سازی سازمانی

* **مدیریت نشست و احراز هویت (User Context):** هنگام ارسال درخواست به گره `erp_assistant`، شناسه‌های دسترسی کاربر (User Role / Claims) را در `AgentState` نگه دارید تا ابزارها دقیقا در سطح دسترسی مجاز کاربر در ERP کوئری بزنند.
* **استفاده از تایید انسانی (Human-in-the-Loop):** از قابلیت `interrupt_before=["erp_tools"]` در LangGraph برای متوقف کردن گراف قبل از اجرای تغییرات حساس در دیتابیس مالی یا انبار استفاده کنید تا تاییدیه کاربر از فرانت‌اند دریافت شود.
* **حفظ حریم داده (Data Masking):** هنگام مسیریابی به `external_ai`، اطلاعات هویتی، ارقام مالی حساس یا کدهای ملی پرسنل را پیش از ارسال با رگولار اکسپرشن یا یک مدل NER سبک به توکن‌های خنثی (مانند `[PERSON_1]`, `[AMOUNT]`) تبدیل کنید.