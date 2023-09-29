from typing import Protocol, cast
import uuid
from sqlalchemy.orm import joinedload

from .base import NotFoundException, Repository
from .models import YugiohSetORM
from app.models import YugiohSet, YugiohCardInSet


class SetRepository(Protocol):
    def get_set_by_id(self, set_id: uuid.UUID) -> YugiohSet:
        pass


class SetNotFound(NotFoundException):
    def __init__(self, set_id: uuid.UUID) -> None:
        super().__init__(f"Did not find set for id: {set_id}")
        self.id = set_id


class YugiohSetRepository(Repository):
    def get_set_by_id(self, set_id: uuid.UUID) -> YugiohSet:
        set: YugiohSetORM | None = (
            self.session.query(YugiohSetORM)
            .options(joinedload(YugiohSetORM.cards))
            .filter(YugiohSetORM.id == set_id)
            .first()
        )

        if set is None:
            raise SetNotFound(set_id)

        return YugiohSet(
            id=cast(uuid.UUID, set.id),
            code=cast(str, set.set_id),
            name=cast(str, set.name),
            cards=[
                YugiohCardInSet(
                    card_id=cast(str, card.card_id),
                    rarity=cast(str, card.rarity),
                    rarity_code=cast(str, card.rarity_code),
                    price=cast(str, card.price),
                )
                for card in set.cards
            ],
        )
