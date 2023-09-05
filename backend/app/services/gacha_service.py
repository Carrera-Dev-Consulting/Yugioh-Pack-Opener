from itertools import groupby

from app.models.yugioh_set import YugiohSet
from app.models.gacha_pull import GachaPull
from app.models.gacha_configuration import (
    GachaConfiguration,
    SingleRarityPool,
    WeightedRarityPool,
    WeightedCollection,
)
from app.models.set_options import SetOptions
from .exceptions.set_exceptions import InvalidSetOptions

from .set_discovery_service import SetDiscoveryService


class GachaService:
    def __init__(self, set_discovery: SetDiscoveryService) -> None:
        self.set_discovery = set_discovery

    def roll_for_set(self, set: YugiohSet) -> GachaPull:
        options = self.set_discovery.discover_set_options(set)
        config = self.build_configuration_from_set_with_options(set, options)
        return config.pull()

    def build_configuration_from_set_with_options(
        self, card_set: YugiohSet, options: SetOptions
    ) -> GachaConfiguration:
        # so we don't have to compute this multiple times
        items_by_rarity = {
            rarity: list(cards)
            for rarity, cards in groupby(card_set.cards, key=lambda c: c.rarity)
        }

        pools = []

        for option in options.options:
            if option.rarity:
                pool = SingleRarityPool(
                    quantity=option.amount_for,
                    cards=items_by_rarity.get(option.rarity, []),
                )
            elif option.weighted_rarities:
                weights = [
                    WeightedCollection(
                        weight=weighted_rarity.weight,
                        cards=items_by_rarity.get(weighted_rarity.rarity, []),
                    )
                    for weighted_rarity in option.weighted_rarities
                ]
                pool = WeightedRarityPool(quantity=option.amount_for, weights=weights)
            else:
                raise InvalidSetOptions(
                    card_set.id, reason="Unable to understand option in set options"
                )

            if len(pool) == 0:
                raise InvalidSetOptions(
                    card_set.id,
                    reason="Unable to find cards for the given option in set options",
                )
            pools.append(pool)

        return GachaConfiguration(pools=pools)
