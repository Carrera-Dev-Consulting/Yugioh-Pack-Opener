import uuid
from .set_exception import SetException


class SetNotFound(SetException):
    def __init__(self, set_id: uuid.UUID) -> None:
        super().__init__(set_id, "No set found for id")
