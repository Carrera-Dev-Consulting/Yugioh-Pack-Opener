from typing import Generic, TypeVar
from .base import Base


class PaginationOptions(Base):
    page: int = 1
    page_size: int = 20


TModel = TypeVar("TModel")


class PaginationResult(Generic[TModel], Base):
    results: list[TModel]
    page: int
    page_size: int
    total: int

    @classmethod
    def from_results(
        cls, results: list[TModel], page_ops: PaginationOptions, total: int
    ):
        return cls(
            results=results,
            page=page_ops.page,
            page_size=page_ops.page_size,
            total=total,
        )
