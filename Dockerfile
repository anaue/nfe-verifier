# ========================= Debian - slim / server profile =============
# FROM tiangolo/uvicorn-gunicorn:python3.9-slim
# RUN apt-get update -y
# RUN apt-get install build-essential -y


# ========================= Alpine / server profile =============
FROM tiangolo/uvicorn-gunicorn:python3.9-alpine3.14

RUN apk add build-base python3-dev py-pip zlib-dev libffi-dev

WORKDIR /app

COPY app/requirements.txt ./

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt


# =============== PRODUCTION  =============
# COPY app/* ./