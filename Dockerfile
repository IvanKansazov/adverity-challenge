FROM python:3.10-alpine

RUN apk update && \
    apk add iputils mysql mysql-client && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add --no-cache mariadb-dev

WORKDIR /var/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
