from fastapi import APIRouter
from fastapi import HTTPException

from src.repositories.task_repository import TaskRepository
from src.schemas.pagination import Pagination
from src.schemas.task import TaskCreateData
from src.schemas.task import TaskDeleteResponse
from src.schemas.task import TaskResponse
from src.schemas.task import TaskUpdateData
from src.services import task_service
from src.services.task_service import TaskOrderBy
from src.utils.convertor import model_to_schema

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=Pagination[TaskResponse])
async def list_tasks(
    page: int = 1,
    per_page: int = 20,
    search: str = None,
    status_id: int = None,
    priority_id: int = None,
    order_by: TaskOrderBy = TaskOrderBy.DEADLINE_DESC,
):
    page = page if page > 0 else 1
    tasks = await task_service.get_tasks(
        offset=(page - 1) * per_page,
        limit=per_page,
        search=search,
        status_id=status_id,
        priority_id=priority_id,
        order_by=order_by,
    )

    tasks_count = await task_service.get_tasks_count(search=search, status_id=status_id, priority_id=priority_id)
    return Pagination(
        items=[model_to_schema(task, TaskResponse) for task in tasks],
        page=page,
        per_page=per_page,
        total=tasks_count,
    )


@router.post("", response_model=TaskResponse, status_code=201)
async def create_task(data: TaskCreateData):
    task = await task_service.create_task(data)
    return model_to_schema(task, TaskResponse)


@router.get("/{task_code}", response_model=TaskResponse)
async def get_task_by_id(task_id: int):
    task = await TaskRepository.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task is not found")
    return model_to_schema(task, TaskResponse)


@router.patch("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, data: TaskUpdateData):
    task = await task_service.update_task(task_id, data)
    if not task:
        raise HTTPException(status_code=404, detail="Task is not found")
    return model_to_schema(task, TaskResponse)


@router.delete("/{task_id}", response_model=TaskDeleteResponse)
async def delete_task(task_id: int):
    deleted_id = await TaskRepository.delete(task_id)
    if not deleted_id:
        raise HTTPException(status_code=404, detail="Task is not found")

    return TaskDeleteResponse(id=deleted_id)
