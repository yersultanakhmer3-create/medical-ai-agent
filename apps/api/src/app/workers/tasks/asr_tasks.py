from __future__ import annotations
from app.workers.celery_app import celery_app

@celery_app.task(name="asr.transcribe_encounter")
def asr_transcribe_encounter(encounter_id: str) -> dict:
    # TODO: implement storage lookup + faster-whisper ASR
    # For now return a stub transcript_id so pipeline can continue.
    return {"encounter_id": encounter_id, "transcript_id": "tr_stub"}
