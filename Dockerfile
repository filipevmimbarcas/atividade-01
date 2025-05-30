FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt update -y

RUN apt install busybox -y


COPY . .

EXPOSE  5000

CMD ["python", "app.py"]
