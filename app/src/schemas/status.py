from pydantic import BaseModel
from pydantic import Field


class StatusResponse(BaseModel):
    id: int
    name: str
    code: str


class StatusDeleteResponse(BaseModel):
    id: int


class StatusUpdateData(BaseModel):
    name: str = Field(min_length=1, max_length=100)


class StatusCreateData(StatusUpdateData):
    code: str = Field(min_length=1, max_length=100)
