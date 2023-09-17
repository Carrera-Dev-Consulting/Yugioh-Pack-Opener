import uuid
from .set_exception import SetException


class NoSetOptions(SetException):
    def __init__(self, set_id: uuid.UUID) -> None:
        super().__init__(set_id, "No options exists for set")
