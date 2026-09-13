from pydantic import BaseModel
from sqlmodel import SQLModel


def model_to_schema[T: BaseModel](model: SQLModel, schema_type: type[T]) -> T:
    return schema_type.model_validate(model.model_dump())
