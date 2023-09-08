from ..base import Base
from pydantic import Field


class PackSelection(Base):
    pack_id: str = Field(
        alias="packId", examples=["3918bc91-2704-42d8-a03c-bc781438c130"]
    )
    total_desired: int = Field(
        alias="totalDesired", examples=[1, 50, 100], ge=1, le=100
    )


class OpenPackRequest(Base):
    selections: list[PackSelection] = Field(
        examples=[
            [
                PackSelection(
                    packId="3918bc91-2704-42d8-a03c-bc781438c130", 
                    totalDesired=1
                )
            ]
        ],
        min_length=1,
    )
