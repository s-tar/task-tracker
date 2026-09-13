from datetime import date
from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    deadline: date | None = None
    status_id: int | None = None
    priority_id: int | None = None
    created_at: datetime
    updated_at: datetime


class TaskUpdateData(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=250)
    description: str | None = Field(max_length=500)
    deadline: date | None = None
    status_id: int | None = None
    priority_id: int | None = None


class TaskCreateData(TaskUpdateData):
    pass


class TaskDeleteResponse(BaseModel):
    id: int
