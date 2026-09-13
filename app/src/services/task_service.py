from enum import Enum

from src.models.task import Task
from src.repositories.priority_repository import PriorityRepository
from src.repositories.status_repository import StatusRepository
from src.repositories.task_repository import TaskRepository
from src.schemas.task import TaskCreateData
from src.schemas.task import TaskUpdateData
from src.utils.validation import validate_entity_exists


class TaskOrderBy(str, Enum):
    DATE_CREATED = "date_created"
    DATE_CREATED_DESC = "date_created_desc"
    DEADLINE = "deadline"
    DEADLINE_DESC = "deadline_desc"
    TITLE = "title"
    TITLE_DESC = "title_desc"


ORDER_BY_FIELDS_MAP = {
    TaskOrderBy.DATE_CREATED: Task.created_at,
    TaskOrderBy.DATE_CREATED_DESC: Task.created_at.desc(),
    TaskOrderBy.DEADLINE: Task.deadline,
    TaskOrderBy.DEADLINE_DESC: Task.deadline.desc().nulls_last(),
    TaskOrderBy.TITLE: Task.title,
    TaskOrderBy.TITLE_DESC: Task.title.desc(),
}


def _prepare_task_filters(
    search: str = None,
    status_id: int = None,
    priority_id: int = None,
):
    filters = []
    if search:
        filters.append(Task.title.icontains(search))

    if status_id:
        filters.append(Task.status_id == status_id)

    if priority_id:
        filters.append(Task.priority_id == priority_id)

    return filters


async def get_tasks(
    offset: int = 0,
    limit: int | None = None,
    search: str = None,
    status_id: int = None,
    priority_id: int = None,
    order_by: TaskOrderBy = TaskOrderBy.DEADLINE_DESC,
) -> list[Task]:
    filters = _prepare_task_filters(search, status_id, priority_id)
    return await TaskRepository.get_list(
        *filters,
        offset=offset,
        limit=limit,
        order_by=[ORDER_BY_FIELDS_MAP[order_by]],
    )


async def get_tasks_count(
    search: str = None,
    status_id: int = None,
    priority_id: int = None,
) -> int:
    filters = _prepare_task_filters(search, status_id, priority_id)
    return await TaskRepository.count(*filters)


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
