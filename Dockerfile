FROM python:3.8-alpine

WORKDIR /usr/src/app
RUN apk update && apk add --no-cache gcc libressl-dev musl-dev libffi-dev build-base

COPY requirements.txt /requirements.txt
RUN pip install -U setuptools 'pip<20' && \
    pip install gunicorn uvloop httptools && \
    pip install -r /requirements.txt

COPY app .

CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
