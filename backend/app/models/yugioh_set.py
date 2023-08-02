import uuid
from backend.app.models.yugioh_card import YugiohCard
from .base import Base


class YugiohSet(Base):
    id: uuid.UUID
    name: str
    cards: list[YugiohCard] = []
