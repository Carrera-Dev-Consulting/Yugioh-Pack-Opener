from .base import Base
from .yugioh_card import YugiohCard


class Pack(Base):
    cards: list[YugiohCard]
