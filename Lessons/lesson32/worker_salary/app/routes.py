from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import WorkersBase

router = APIRouter()


@router.get("/workers/")
def get_workers_all():
    return {"message": "workers"}


@router.get("/workers/{worker_id}")
def get_worker_by_id(worker_id, worker_db: WorkersBase, db : Session = Depends(get_db)):  # noqa: B008
    worker = db.query(worker_db).filter(worker_db.id == worker_id).first()

    return {"message": "Get worker by id", "data": worker}
