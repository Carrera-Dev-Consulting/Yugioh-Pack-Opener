from collections import defaultdict

from app.models import YugiohSet, SetOptions
from app.models.set_options import DEFAULT_SET_OPTIONS

from .exceptions.set_exceptions import NoSetOptions


class SetDiscoveryService:
    def __init__(self, set_to_options: dict[str, SetOptions] | None = None) -> None:
        self.set_to_options: dict[str, SetOptions] = defaultdict(
            lambda: DEFAULT_SET_OPTIONS
        )
        if set_to_options:
            self.set_to_options.update(set_to_options)

    def discover_set_options(self, set: YugiohSet) -> SetOptions:
        value = self.set_to_options[set.code]
        if value is None:
            raise NoSetOptions(set_id=set.id)

        return value
