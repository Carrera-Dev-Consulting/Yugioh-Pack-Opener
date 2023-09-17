from .base import Base
from .yugioh_card import YugiohCard


class Pack(Base):
    cards: list[YugiohCard]

    def __iter__(self):
        for card in self.cards:
            yield card
