import uuid
from .set_exception import SetException


class InvalidSetOptions(SetException):
    def __init__(self, set_id: uuid.UUID, reason: str) -> None:
        super().__init__(set_id, f"Set options could not be understood, {reason}")
        self.reason = reason
