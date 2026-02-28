from __future__ import annotations

import os
from celery import Celery

BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/1")

celery_app = Celery("medical_ai_agent", broker=BROKER_URL, backend=RESULT_BACKEND)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_track_started=True,
    task_time_limit=60 * 20,
    worker_prefetch_multiplier=1,
)

# IMPORTANT:
# autodiscover expects "<package>.tasks" modules.
# Therefore we pass "app.workers" so Celery imports "app.workers.tasks".
celery_app.autodiscover_tasks(["app.workers"], force=True)
