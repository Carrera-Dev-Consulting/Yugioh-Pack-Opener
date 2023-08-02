from uuid import UUID
from .base import Base


class YugiohSetInfo(Base):
    rarity: str
    rarity_code: str
    price: str


class YugiohCard(Base):
    id: UUID
    name: str
    type: str
    description: str
    archetype: str | None
    race: str | None
    sets: list[YugiohSetInfo] = []
