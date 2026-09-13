from datetime import datetime

from sqlalchemy import func
from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from src.models.priority import Priority
from src.models.status import Status


class Task(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    description: str | None = None
    deadline: datetime | None = None
    status_id: int = Field(foreign_key="status.id")
    priority_id: int = Field(foreign_key="priority.id")
    created_at: datetime = Field(sa_column_kwargs={
        "default": func.now(),
        "server_default": func.now(),
    })
    updated_at: datetime = Field(sa_column_kwargs={
        "default": func.now(),
        "onupdate": func.now(),
        "server_default": func.now(),
    })

    status: Status = Relationship(back_populates="tasks")
    priority: Priority = Relationship(back_populates="tasks")
