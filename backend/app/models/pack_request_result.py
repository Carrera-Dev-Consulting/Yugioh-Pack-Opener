from .base import Base
from .pack import Pack


class PackRequestResult(Base):
    cards_pulled: list[Pack]

    def __iter__(self):
        for pack in self.cards_pulled:
            for card in pack:
                yield card
