from datetime import datetime, time

from pydantic import BaseModel


class WorkersBase(BaseModel):
    full_name: str
    phone_number: str
    salary: float
    shift_start: time
    shift_end: time
    major: str
    rejim: str


class SalaryBase(BaseModel):
    amount: str
    worker_id: int


class AttendanceBase(BaseModel):
    work_day: datetime
    worker_id: int
    status: bool


class FineBase(BaseModel):
    amount: float
    comment: str
    worker_id: int
