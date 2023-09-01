from itertools import groupby

from app.models.yugioh_set import YugiohSet
from app.models.gacha_pull import GachaPull


class GachaService:
    def __init__(self) -> None:
        pass

    def roll_for_set(self, set: YugiohSet) -> GachaPull:
        groupby()
