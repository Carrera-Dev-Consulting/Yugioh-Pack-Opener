from uuid import UUID
from .base import Base


class YugiohSetInfo(Base):
    set_id: str
    rarity: str
    rarity_code: str
    price: str | None


class YugiohCard(Base):
    id: UUID
    name: str
    type: str
    description: str
    archetype: str | None
    race: str | None
    sets: list[YugiohSetInfo] = []
