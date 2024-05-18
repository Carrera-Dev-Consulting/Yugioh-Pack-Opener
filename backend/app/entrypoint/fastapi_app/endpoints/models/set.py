from datetime import date
from typing import Annotated

from fastapi import Query
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from app.models.set_request import SetRequest


def set_request(
    set_ids: Annotated[
        list[str] | None,
        Query(
            description="Ids of sets you are wanting to look for.",
        ),
    ] = [],
    end_date: Annotated[
        date | None,
        Query(
            description="The upper limit of when you want the set to have been released",
        ),
    ] = None,
    start_date: Annotated[
        date | None,
        Query(
            description="The lower limit of when you want the set to have been released",
        ),
    ] = None,
):
    if start_date and end_date and start_date > end_date:
        raise RequestValidationError(errors=["Start date must be less then end date."])
    return SetRequest(set_ids=set_ids, end_date=end_date, start_date=start_date)
