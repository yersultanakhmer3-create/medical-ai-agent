from __future__ import annotations
from app.workers.celery_app import celery_app

@celery_app.task(name="note.generate_dental_note")
def generate_dental_note(payload: dict) -> dict:
    # TODO: implement LLM generation + pydantic validation + store note_version_id
    return {
        "encounter_id": payload["encounter_id"],
        "transcript_id": payload["transcript_id"],
        "note_version_id": "note_stub",
    }
