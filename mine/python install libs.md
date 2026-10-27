

(Ok - tested) pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn     fastapi uvicorn pydantic sqlalchemy redis celery     langchain openai anthropic sentence-transformers

pip install -i https://mirror-pypi.runflare.com/simple --trusted-host mirror-pypi.runflare.com     fastapi uvicorn pydantic sqlalchemy redis celery     langchain openai anthropic sentence-transformers


mkdir -p /opt/assistant && cd /opt/assistant
python3 -m venv venv && source venv/bin/activate

pip install fastapi uvicorn pydantic sqlalchemy redis celery \
    langchain openai anthropic sentence-transformers

