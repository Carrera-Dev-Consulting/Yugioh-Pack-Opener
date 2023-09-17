from datetime import datetime
import uuid
from .base import Base


class YugiohCardInSet(Base):
    card_id: str
    rarity: str
    rarity_code: str
    price: str | None


class SetImage(Base):
    regular_url: str


class YugiohSet(Base):
    id: uuid.UUID
    code: str
    name: str
    release_date: datetime | None = None
    card_count: int = 0
    cards: list[YugiohCardInSet] = []
    image: SetImage | None = None
