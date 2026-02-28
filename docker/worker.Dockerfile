FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl \
  && rm -rf /var/lib/apt/lists/*

COPY apps/api/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -r /app/requirements.txt

COPY apps/api/src /app/src
ENV PYTHONPATH=/app/src
WORKDIR /app/src

CMD ["celery", "-A", "app.workers.celery_app:celery_app", "worker", "-l", "info"]
