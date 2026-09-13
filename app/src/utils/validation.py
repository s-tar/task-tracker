from src.exceptions import NotFoundValidationError
from src.repositories.base_repository import BaseRepository


async def validate_entity_exists[T](repo: BaseRepository[T], entity_id: int) -> bool:
    if not await repo.exists(repo.table_model.id == entity_id):
        raise NotFoundValidationError(
            field_name="status_id",
            field_value=entity_id,
            message=f"{repo.table_model.__name__} {entity_id} is not found.",
        )
