from pydantic import BaseModel
from pydantic import Field


class PriorityResponse(BaseModel):
    id: int
    name: str
    code: str


class PriorityDeleteResponse(BaseModel):
    id: int


class PriorityUpdateData(BaseModel):
    name: str = Field(min_length=1, max_length=100)


class PriorityCreateData(PriorityUpdateData):
    code: str = Field(min_length=1, max_length=100)
