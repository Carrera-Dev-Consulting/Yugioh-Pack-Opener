from typing import TypeVar, Generic
from .base import Base

T = TypeVar("T")


class Result(Base, Generic[T]):
    value: T | None = None
    errors: list[str] = []
