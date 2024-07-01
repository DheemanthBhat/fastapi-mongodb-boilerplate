FROM tiangolo/uvicorn-gunicorn:python3.11-slim

EXPOSE 80

WORKDIR /app

COPY ./src src/
COPY ./requirements.txt .

RUN pip install -r ./requirements.txt
