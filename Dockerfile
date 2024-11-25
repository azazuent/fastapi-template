FROM python:latest

WORKDIR /app

COPY src/ /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "src:app_v1"]
