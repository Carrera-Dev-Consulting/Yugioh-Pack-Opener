from uuid import UUID
from fastapi import Query

from app.models.yugioh_card import YugiohCardType
from .base import Base


class APIQuery(Base):
    page: int = Query(default=1, description="The page you are looking at")
    size: int = Query(default=50, description="The total amount of records to return")


class CardQuery(APIQuery):
    name: str | None = Query(
        None, description="The name of the card you are looking for"
    )
    kind: YugiohCardType | None = Query(
        None,
        description="The kind of card you are looking for I.E. Effect, Normal, Spell Card etc..",
    )
    id: UUID | None = Query(None, description="Yugioh Card Id to get specific card")
    archetype: str | None = Query(
        None,
        description="The archetype of the cards you are looking for i.e. Spriggans, Super Heavy Samurai's, etc...",
    )
    race: str | None = Query(
        None,
        description="The race of the monster card you are looking for i.e. Fiend, Warrior, Beast-Warrior",
    )
    defense: int | None = Query(None, description="Defense points of a card.")
    attack: int | None = Query(None, description="Attack points of a card.")
    attribute: str | None = Query(
        None, description="The attribute of the monster card you are looking for"
    )
    level: int | None = Query(None, description="The Level on the card")
    link_value: int | None = Query(
        None, description="Link value that the card is when linking"
    )
    ban_level: str | None = Query(
        None,
        description="Ban Level for the card if any i.e. Limited, Semi-Limited, Banned",
    )
