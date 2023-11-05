from app.models import User
from .general_exceptions import MissingElement, InvalidElement


class UserNotFound(MissingElement):
    def __init__(self, id: str) -> None:
        super().__init__(User, id)


class InvalidUser(InvalidElement):
    def __init__(self, reasons: list[str]) -> None:
        super().__init__(User, reasons)
