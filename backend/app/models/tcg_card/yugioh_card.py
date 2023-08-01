from app.models.base import Base
from .tcg_card import TCGCard

class YugiohCardMetadata(Base):
    type: str
    archetype: str
    race: str    


class YugiohCard(TCGCard):
    metadata: YugiohCardMetadata