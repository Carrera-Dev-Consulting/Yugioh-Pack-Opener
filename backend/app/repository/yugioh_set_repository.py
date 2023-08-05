from typing import Protocol
from sqlalchemy.orm import joinedload

from .base import NotFoundException, Repository
from .models import YugiohSetORM
from app.models import YugiohSet, YugiohCardInSet


class SetRepository(Protocol):
    def get_set_by_id(self, set_id: str) -> YugiohSet:
        pass


class SetNotFound(NotFoundException):
    def __init__(self, set_id: str) -> None:
        super().__init__(f"Did not find set for id: {set_id}")
        self.id = set_id


class YugiohSetRepository(Repository):
    def get_set_by_id(self, set_id: str) -> YugiohSet:
        set: YugiohSetORM = (
            self.session.query(YugiohSetORM)
            .options(joinedload(YugiohSetORM.cards))
            .filter(YugiohSetORM.id == set_id)
            .first()
        )

        if set is None:
            raise SetNotFound(set_id)

        return YugiohSet(
            id=set.id,
            name=set.name,
            cards=[
                YugiohCardInSet(
                    card_id=card.card_id,
                    rarity=card.rarity,
                    rarity_code=card.rarity_code,
                    price=card.price,
                )
                for card in set.cards
            ],
        )
