from typing import Annotated
from fastapi import Query
from pydantic import BaseModel, ConfigDict

from app.models.pagination import PaginationOptions


class Base(BaseModel):
    model_config = ConfigDict(frozen=True)


def page_parameters(
    page: Annotated[
        int,
        Query(
            description="The page you are looking at in your query.",
            ge=0,
            example=1,
        ),
    ] = 1,
    page_size: Annotated[
        int,
        Query(
            description="The max amount of records you want in a given page.",
            ge=0,
            le=100_000,
            alias="pageSize",
            example=50,
        ),
    ] = 20,
):
    return PaginationOptions(page=page, page_size=page_size)
