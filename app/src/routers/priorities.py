from fastapi import APIRouter
from fastapi import HTTPException

from src.exceptions import NotUniqueValidationError
from src.models.task import Task
from src.repositories.priority_repository import PriorityRepository
from src.repositories.task_repository import TaskRepository
from src.schemas.priority import PriorityCreateData
from src.schemas.priority import PriorityDeleteResponse
from src.schemas.priority import PriorityResponse
from src.schemas.priority import PriorityUpdateData
from src.utils.convertor import model_to_schema

router = APIRouter(prefix="/priorities", tags=["Priorities"])


@router.get("", response_model=list[PriorityResponse])
async def list_priorities():
    priorities = await PriorityRepository.get_list()
    return [model_to_schema(priority, PriorityResponse) for priority in priorities]


@router.post("", response_model=PriorityResponse, status_code=201)
async def create_priority(data: PriorityCreateData):
    if PriorityRepository.get_by_code(data.code):
        raise NotUniqueValidationError(
            field_name="code",
            field_value=data.code,
            message=f"Priorities with a code '{data.code}' already exists.",
        )
    priority = await PriorityRepository.create(data.model_dump())
    return model_to_schema(priority, PriorityResponse)


@router.get("/{priority_id}", response_model=PriorityResponse)
async def get_priority_by_id(priority_id: int):
    priority = await PriorityRepository.get_by_id(priority_id)
    if not priority:
        raise HTTPException(status_code=404, detail="Priorities is not found")
    return model_to_schema(priority, PriorityResponse)


@router.get("/code/{priority_code}", response_model=PriorityResponse)
async def get_priority_by_code(priority_code: str):
    priority = await PriorityRepository.get_by_code(priority_code)
    if not priority:
        raise HTTPException(status_code=404, detail="Priorities is not found")
    return model_to_schema(priority, PriorityResponse)


@router.patch("/{priority_id}", response_model=PriorityResponse)
async def update_priority(priority_id: int, data: PriorityUpdateData):
    priority = await PriorityRepository.update(priority_id, data=data.model_dump(exclude_unset=True))
    if not priority:
        raise HTTPException(status_code=404, detail="Priorities is not found")

    return model_to_schema(priority, PriorityResponse)


@router.delete("/{priority_id}", response_model=PriorityDeleteResponse)
async def delete_priority(priority_id: int):
    if await TaskRepository.get_list(Task.priority_id == priority_id):
        raise HTTPException(status_code=400, detail="Failed to delete. Priorities is used by Task.")

    deleted_id = await PriorityRepository.delete(priority_id)
    if not deleted_id:
        raise HTTPException(status_code=404, detail="Priorities is not found")

    return PriorityDeleteResponse(id=deleted_id)
