from pydantic import BaseModel


class Pagination[T](BaseModel):
    items: list[T]
    page: int = 1
    per_page: int = 20
    total: int = 0
