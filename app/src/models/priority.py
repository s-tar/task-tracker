from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from src.models.task import Task


class Priority(SQLModel, table=True):
    id: int = Field(primary_key=True)
    code: str = Field(unique=True)
    name: str = Field()

    tasks: list["Task"] = Relationship(back_populates="priority")
