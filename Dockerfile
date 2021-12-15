FROM python:3

ENV PYTHONBUFFERED 1

# RUN apk update \
#     && apk add --virtual build-essential gcc python3-dev musl-dev \
#     && apk add postgresql-dev \
#     && pip install psycopg2


WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .
