from .base import Base


CardId = str


class GachaPull(Base):
    results: list[CardId]
