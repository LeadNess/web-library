FROM python:3.6.8-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && apk add zlib libjpeg jpeg-dev zlib-dev \
    && pip install --upgrade pip \
    && pip install psycopg2 Pillow

COPY requirements.txt /code/
RUN pip install -r code/requirements.txt \
    && apk del --no-cache build-deps

COPY library /library
COPY deploy/container_settings /library/library/settings.py
COPY deploy/migrations /migrations

COPY deploy/entrypoint.sh /entrypoint.sh
RUN chmod 777 /entrypoint.sh
CMD ["/bin/sh", "/entrypoint.sh"]
