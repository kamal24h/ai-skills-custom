from langchain_community.llms import Ollama

llm = Ollama(
    base_url="http://ollama:11434",
    model="deepseek-r1:7b-q4_K_M",
    temperature=0.7,
    num_ctx=4096  # تنظیم طول کانتکست برای مدیریت حافظه VRAM
)