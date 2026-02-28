from __future__ import annotations

from celery import chain
from app.workers.celery_app import celery_app
from app.workers.tasks.asr_tasks import asr_transcribe_encounter
from app.workers.tasks.note_tasks import generate_dental_note
from app.workers.tasks.evidence_tasks import link_evidence_for_note

@celery_app.task(name="pipeline.process_encounter")
def process_encounter(encounter_id: str) -> dict:
    workflow = chain(
        asr_transcribe_encounter.s(encounter_id),
        generate_dental_note.s(),
        link_evidence_for_note.s(),
    )
    ar = workflow.apply_async()
    return {"encounter_id": encounter_id, "workflow_task_id": ar.id}
