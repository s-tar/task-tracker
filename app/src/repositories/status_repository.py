from src.models.status import Status
from src.repositories.base_repository import BaseRepository


class StatusRepositoryClass(BaseRepository[Status]):
    def __init__(self):
        super().__init__(Status)

    async def get_by_code(self, code: str):
        return await self.get(Status.code == code)


StatusRepository = StatusRepositoryClass()
