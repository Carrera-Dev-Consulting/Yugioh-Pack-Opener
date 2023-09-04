from collections import defaultdict

from app.models import YugiohSet, SetOptions
from app.models.set_options import DEFAULT_SET_OPTIONS


class SetDiscoveryService:
    def __init__(self, set_to_options: dict[str, SetOptions]) -> None:
        self.set_to_options = defaultdict(lambda: DEFAULT_SET_OPTIONS)
        self.set_to_options.update(set_to_options)

    def dicover_set_options(self, set: YugiohSet) -> SetOptions:
        return self.set_to_options[set.code]
