from fastapi import APIRouter
from fastapi import HTTPException

from src.exceptions import NotUniqueValidationError
from src.models.task import Task
from src.repositories.status_repository import StatusRepository
from src.repositories.task_repository import TaskRepository
from src.schemas.status import StatusCreateData
from src.schemas.status import StatusDeleteResponse
from src.schemas.status import StatusResponse
from src.schemas.status import StatusUpdateData
from src.utils.convertor import model_to_schema

router = APIRouter(prefix="/statuses", tags=["Statuses"])


@router.get("", response_model=list[StatusResponse])
async def list_statuses():
    statuses = await StatusRepository.get_list()
    return [model_to_schema(status, StatusResponse) for status in statuses]


@router.post("", response_model=StatusResponse, status_code=201)
async def create_status(data: StatusCreateData):
    if StatusRepository.get_by_code(data.code):
        raise NotUniqueValidationError(
            field_name="code",
            field_value=data.code,
            message=f"Statuses with a code '{data.code}' already exists.",
        )
    status = await StatusRepository.create(data.model_dump())
    return model_to_schema(status, StatusResponse)


@router.get("/{status_id}", response_model=StatusResponse)
async def get_status_by_id(status_id: int):
    status = await StatusRepository.get_by_id(status_id)
    if not status:
        raise HTTPException(status_code=404, detail="Statuses is not found")
    return model_to_schema(status, StatusResponse)


@router.get("/code/{status_code}", response_model=StatusResponse)
async def get_status_by_code(status_code: str):
    status = await StatusRepository.get_by_code(status_code)
    if not status:
        raise HTTPException(status_code=404, detail="Statuses is not found")
    return model_to_schema(status, StatusResponse)


@router.patch("/{status_id}", response_model=StatusResponse)
async def update_status(status_id: int, data: StatusUpdateData):
    status = await StatusRepository.update(status_id, data=data.model_dump(exclude_unset=True))
    if not status:
        raise HTTPException(status_code=404, detail="Statuses is not found")

    return model_to_schema(status, StatusResponse)


@router.delete("/{status_id}", response_model=StatusDeleteResponse)
async def delete_status(status_id: int):
    if await TaskRepository.get_list(Task.status_id == status_id):
        raise HTTPException(status_code=400, detail="Failed to delete. Statuses is used by Task.")

    deleted_id = await StatusRepository.delete(status_id)
    if not deleted_id:
        raise HTTPException(status_code=404, detail="Statuses is not found")

    return StatusDeleteResponse(id=deleted_id)
