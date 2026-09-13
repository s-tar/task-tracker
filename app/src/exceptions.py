from fastapi.exceptions import RequestValidationError
from pydantic_core import ErrorDetails


class NotUniqueValidationError(RequestValidationError):
    def __init__(self, field_name: str, field_value: any, message: str):
        super().__init__(
            [ErrorDetails(
                type="not_unique",
                msg=message,
                loc=("body", field_name),
                input=field_value,
            )],
        )


class NotFoundValidationError(RequestValidationError):
    def __init__(self, field_name: str, field_value: any, message: str):
        super().__init__(
            [ErrorDetails(
                type="not_found",
                msg=message,
                loc=("body", field_name),
                input=field_value,
            )],
        )
