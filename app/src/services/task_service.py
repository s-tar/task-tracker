from src.models.task import Task
from src.repositories.priority_repository import PriorityRepository
from src.repositories.status_repository import StatusRepository
from src.repositories.task_repository import TaskRepository
from src.schemas.task import TaskCreateData
from src.schemas.task import TaskUpdateData
from src.utils.validation import validate_entity_exists


async def create_task(data: TaskCreateData):
    await validate_entity_exists(repo=StatusRepository, entity_id=data.status_id)
    await validate_entity_exists(repo=PriorityRepository, entity_id=data.priority_id)
    return await TaskRepository.create(data.model_dump())


async def update_task(task_id: int, data: TaskUpdateData) -> Task | None:
    task = await TaskRepository.get_by_id(task_id)
    if not task:
        return None

    if data.status_id:
        await validate_entity_exists(repo=StatusRepository, entity_id=data.status_id)

    if data.priority_id:
        await validate_entity_exists(repo=PriorityRepository, entity_id=data.priority_id)

    return await TaskRepository.update(entity_id=task_id, data=data.model_dump(exclude_unset=True))
