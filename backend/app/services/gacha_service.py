from itertools import groupby

from app.models.yugioh_set import YugiohSet
from app.models.gacha_pull import GachaPull
from app.models.gacha_configuration import GachaConfiguration
from app.models.set_options import SetOptions

from .set_discovery_service import SetDiscoveryService


class GachaService:
    def __init__(self, set_discovery: SetDiscoveryService) -> None:
        self.set_discovery = set_discovery

    def roll_for_set(self, set: YugiohSet) -> GachaPull:
        options = self.set_discovery.dicover_set_options(set)
        config = self.build_configuration_from_set_with_options(set, options)
        return config.pull()

    def build_configuration_from_set_with_options(
        self, set: YugiohSet, options: SetOptions
    ) -> GachaConfiguration:
        pass
