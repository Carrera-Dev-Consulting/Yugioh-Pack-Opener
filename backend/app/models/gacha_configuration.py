from dataclasses import dataclass, field
import random
from typing import Protocol

from .base import Base
from .yugioh_set import YugiohCardInSet
from .gacha_pull import GachaPull


class SingleRarityPool(Base):
    """Defines a pool of a single rarity that will be used for situtations like a set amount of common and rare cards

    Args:
        quantity (int): Amount of cards that will be pulled from the collection
        cards (list[YugiohCardInSet]): Cards in pool that can be selected.
    """

    quantity: int
    cards: list[YugiohCardInSet]

    def _pick_card(self, random_range=random.randrange):
        index = random_range(0, len(self.cards))
        pick = self.cards[index]
        del self.cards[index]
        return pick

    def pull(self, random_range=random.randrange) -> list[YugiohCardInSet]:
        """Generates a pull from the collection of cards that are here for the amount defined in quantity.

        Args:
            random_range (random.randrange, optional): Random function used to select value in collection. Defaults to random.randrange.

        Returns:
            list[YugiohCardInSet]: List of cards that have been removed from the pool
        """
        return [
            self._pick_card(random_range=random_range) for _ in range(self.quantity)
        ]


class WeightedCollection(Base):
    """Weighted collection of cards used by the WeightedRarityPool that exposes a way to select a single
    card from the selection

    Args:
        cards (list[YugiohCardInSet]): cards in the collection
        weight (float): the value representing how frequently this item should appear
    """

    cards: list[YugiohCardInSet]
    weight: float

    def pick(self, random_range=random.randrange) -> YugiohCardInSet:
        """Selects and removes a YugiohCardInSet object from the backing collection.
        Args:
            random_range (random.randrange, optional): Random function used to select the specific card from the collection. Defaults to random.randrange.

        Returns:
            YugiohCardInSet: card that was selected randomly
        """
        index = random_range(0, len(self.cards))
        pick = self.cards[index]
        del self.cards[index]
        return pick


class WeightedRarityPool(Base):
    """Pool that uses a collection of weights that allows cards to be picked from their subset of cards.
    This is used when we have selection of rarities for a specific slot in a pack for the higher rarity cards
    that could also be commons.

    Args:
        quantity (int): amount of cards that will be generated from the pull method
        weights (list[Weight]): list of different weights that have been defined in pool
    """

    quantity: int
    weights: list[WeightedCollection]

    def pick_weight(self, random_float=random.uniform) -> WeightedCollection:
        """Selects the specific weight that will be used in the pull for a specific pick

        Args:
            random_float (random.uniform, optional): random_function that is used to determine. Defaults to random.uniform.

        Raises:
            ValueError: _description_

        Returns:
            WeightedCollection: _description_
        """
        total_weight = sum([weight.weight for weight in self.weights])
        if total_weight == 0:
            raise ValueError("No items to weigh")

        selected_value = random_float(0, total_weight)
        current_weight = 0
        for weight in sorted(self.weights, key=lambda k: k.weight):
            current_weight += weight.weight
            if current_weight > selected_value:
                return weight

    def pull(
        self, random_float=random.uniform, random_range=random.randrange
    ) -> list[YugiohCardInSet]:
        """Generate a pull for the gacha system from the weighted collections using the weights to determine how rarities are selected.

        Args:
            random_float (random.uniform, optional): function to generate random float which is used to select the specific weights. Defaults to random.uniform.
            random_range (random.randrange, optional): function to generate random int from range which is used to select card from weighted pool. Defaults to random.randrange.

        Returns:
            list[YugiohCardInSet]: Selected cards for the most recent pull from the pool
        """
        return [
            self.pick_weight(random_float=random_float).pick(random_range=random_range)
            for _ in range(self.quantity)
        ]


class Pool(Protocol):
    """Definition of Card Pool which allows people to pull cards based on pool configuration"""

    def pull() -> list[YugiohCardInSet]:
        pass


@dataclass
class GachaConfiguration:
    pools: list[Pool] = field()

    def pull(self) -> GachaPull:
        cards = [card.card_id for pool in self.pools for card in pool.pull()]
        return GachaPull(results=cards)
