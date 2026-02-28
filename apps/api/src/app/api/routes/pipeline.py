from fastapi import APIRouter
from pydantic import BaseModel, constr

from app.workers.tasks.pipeline import process_encounter

router = APIRouter(tags=["pipeline"])

class ProcessRequest(BaseModel):
    encounter_id: constr(min_length=3)

@router.post("/pipeline/process")
def start_pipeline(req: ProcessRequest):
    r = process_encounter.delay(req.encounter_id)
    return {"encounter_id": req.encounter_id, "task_id": r.id}
