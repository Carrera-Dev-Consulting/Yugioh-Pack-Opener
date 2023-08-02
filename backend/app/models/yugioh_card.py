from uuid import UUID
from .base import Base


class SetReference(Base):
    pass


class YugiohCard(Base):
    id: UUID
    name: str
    type: str
    description: str
    archetype: str | None
    race: str | None
