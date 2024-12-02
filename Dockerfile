FROM python:latest

WORKDIR /app

COPY app/ /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
