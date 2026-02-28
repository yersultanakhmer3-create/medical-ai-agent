from __future__ import annotations
from app.workers.celery_app import celery_app

@celery_app.task(name="evidence.link_for_note")
def link_evidence_for_note(payload: dict) -> dict:
    # TODO: implement evidence linking (pgvector)
    return {
        "encounter_id": payload["encounter_id"],
        "note_version_id": payload["note_version_id"],
        "evidence_links_created": 0,
    }
