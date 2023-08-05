import uuid
from .base import Base


class YugiohCardInSet(Base):
    card_id: str
    rarity: str
    rarity_code: str
    price: str | None


class YugiohSet(Base):
    id: uuid.UUID
    name: str
    cards: list[YugiohCardInSet] = []
