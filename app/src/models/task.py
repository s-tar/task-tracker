from datetime import datetime

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
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    status: Status = Relationship(back_populates="tasks")
    priority: Priority = Relationship(back_populates="tasks")
