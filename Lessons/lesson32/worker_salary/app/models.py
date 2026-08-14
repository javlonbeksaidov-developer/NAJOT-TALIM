from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    Time,
)
from sqlalchemy.orm import relationship

from app.database import Base


class Workers(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(length=55))
    phone_number = Column(String(length=10))
    salary = Column(Float)
    shift_start = Column(Time)
    shift_end = Column(Time)
    major = Column(String(length=50))
    rejim = Column(String)
    created_at = Column(DateTime)

    salary_table = relationship("Salaries", back_populates="worker")
    attendance_table = relationship("Attendances", back_populates="worker")
    fine_table = relationship("Fines", back_populates="worker")


class Salaries(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    worker_id = Column(Integer, ForeignKey("workers.id"))

    worker = relationship("Workers", back_populates="salary_table")


class Attendances(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True)
    work_day = Column(DateTime)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    status = Column(Boolean)
    created_at = Column(DateTime)

    worker = relationship("Workers", back_populates="salary_table")


class Fines(Base):
    __tablename__ = "fines"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    created_at = Column(DateTime)
    comment = Column(Text)
    worker_id = Column(Integer, ForeignKey("workers.id"))

    worker = relationship("Workers", back_populates="salary_table")
