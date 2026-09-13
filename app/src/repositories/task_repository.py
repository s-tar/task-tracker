from src.models.task import Task
from src.repositories.base_repository import BaseRepository


class TaskRepositoryClass(BaseRepository[Task]):
    def __init__(self):
        super().__init__(Task)


TaskRepository = TaskRepositoryClass()
