from typing import Protocol
from sqlalchemy.orm import joinedload

from .base import Repository
from .models import YugiohCardORM
from app.models import YugiohCard, YugiohSetInfo


class CardRepository(Protocol):
    def get_cards_for_ids(card_ids: list[str]) -> list[YugiohCard]:
        pass


def orm_to_domain_model(orm_model: YugiohCardORM) -> YugiohCardORM:
    card = YugiohCard.model_validate(orm_model)
    # format the sets to the object model expected for the api.
    card.sets = [YugiohSetInfo.model_validate(value) for value in card.sets]
    return card


class YugiohCardRepository(Repository):
    def get_all(self) -> list[YugiohCard]:
        items: list[YugiohCardORM] = self._query().all()
        return [orm_to_domain_model(record) for record in items]

    def _query(self):
        return self.session.query(YugiohCardORM).option(joinedload(YugiohCardORM.sets))

    def query_cards(self, name=None, type=None, **kwargs) -> list[YugiohCard]:
        # add explicit calls to be able to filter down items to specific models
        return self.get_all()
