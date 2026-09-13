from src.models.priority import Priority
from src.repositories.base_repository import BaseRepository


class PriorityRepositoryClass(BaseRepository[Priority]):
    def __init__(self):
        super().__init__(Priority)

    async def get_by_code(self, code: str):
        return await self.get(Priority.code == code)


PriorityRepository = PriorityRepositoryClass()
