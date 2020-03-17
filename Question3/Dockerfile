FROM python:3.7-alpine

ENV PYTHONBUFFERED 1
ENV C_FORCE_ROOT true
STOPSIGNAL SIGTERM

RUN apk add --virtual build-deps gcc libffi-dev libevent-dev python3-dev musl-dev jpeg-dev zlib-dev libcurl curl-dev

WORKDIR /app

RUN pip install -U pip && \
    pip install pipenv

COPY ./Pipfile Pipfile
COPY ./Pipfile.lock Pipfile.lock
COPY ./entrypoint.sh /app/entrypoint.sh

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

ADD . /app

RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["sh","/app/entrypoint.sh"]
