# Ensure Celery registers tasks on worker startup.
from app.workers.tasks.pipeline import process_encounter  # noqa: F401
from app.workers.tasks.asr_tasks import asr_transcribe_encounter  # noqa: F401
from app.workers.tasks.note_tasks import generate_dental_note  # noqa: F401
from app.workers.tasks.evidence_tasks import link_evidence_for_note  # noqa: F401
