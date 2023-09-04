import random

from .base import Base
from .yugioh_set import YugiohCardInSet
from .gacha_pull import GachaPull


class Pool(Base):
    quantity: int
    cards: list[YugiohCardInSet]

    def _pick_card(self):
        index = random.randrange(0, len(self.cards))
        pick = self.cards[index]
        del self.cards[index]
        return pick

    def pull(self) -> list[YugiohCardInSet]:
        return [self._pick_card() for _ in range(self.quantity)]


class Weight(Base):
    cards: list[YugiohCardInSet]
    weight: float

    def pick(self) -> YugiohCardInSet:
        index = random.randrange(0, len(self.cards))
        pick = self.cards[index]
        del self.cards[index]
        return pick


class WeightedPool(Base):
    quantity: int
    weights: list[Weight]

    def pick_weight(self, random_float=random.uniform) -> Weight:
        total_weight = sum([weight.weight for weight in self.weights])
        if total_weight == 0:
            raise ValueError("No items to weigh")

        selected_value = random_float(0, total_weight)
        current_weight = 0
        for weight in sorted(self.weights, key=lambda k: k.weight):
            current_weight += weight.weight
            if current_weight > selected_value:
                return weight

    def pull(self) -> list[YugiohCardInSet]:
        return [self._pick_weight().pick() for _ in range(self.quantity)]


class GachaConfiguration(Base):
    card_pools: list[Pool | WeightedPool]

    def pull(self) -> GachaPull:
        cards = [card.card_id for pool in self.card_pools for card in pool.pull()]
        return GachaPull(results=cards)
