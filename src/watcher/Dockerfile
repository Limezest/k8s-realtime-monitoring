FROM python:3.7-alpine
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["/usr/local/bin/python", "/app/main.py"]