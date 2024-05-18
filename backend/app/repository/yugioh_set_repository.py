from datetime import date
from typing import Protocol, cast
from urllib.parse import quote
import uuid
from sqlalchemy.orm import joinedload

from app.models.yugioh_set import SetImage

from .base import NotFoundException, Repository, QueryResult
from .models import YugiohSetORM
from app.models import YugiohSet, YugiohCardInSet


class SetRepository(Protocol):
    def get_set_by_id(self, set_id: uuid.UUID) -> YugiohSet:
        pass

    def get_sets(
        self,
        *,
        offset: int,
        limit: int,
        start_date: date | None,
        end_date: date | None,
        set_ids: list[str],
    ) -> QueryResult[YugiohSet]:
        pass


class SetNotFound(NotFoundException):
    def __init__(self, set_id: uuid.UUID) -> None:
        super().__init__(f"Did not find set for id: {set_id}")
        self.id = set_id


def orm_to_model(orm: YugiohSetORM) -> YugiohSet:
    return YugiohSet(
        id=orm.id,
        name=orm.name,
        release_date=orm.release_date,
        code=orm.set_id,
        card_count=orm.card_count,
        cards=[],
        image=SetImage(
            regular_url=quote(f"/images/{orm.set_id}.jpg"),
        ),
    )


class YugiohSetRepository(Repository):
    def get_sets(
        self,
        *,
        offset: int,
        limit: int,
        start_date: date | None,
        end_date: date | None,
        set_ids: list[str],
    ) -> QueryResult[YugiohSet]:

        base_query = self.session.query(YugiohSetORM)

        if start_date is not None:
            base_query = base_query.filter(YugiohSetORM.release_date >= start_date)

        if end_date is not None:
            base_query = base_query.filter(YugiohSetORM.release_date <= end_date)

        if set_ids:
            base_query = base_query.filter(YugiohSetORM.id.in_(set_ids))

        results = base_query.limit(limit).offset(offset).all()
        total = base_query.count()

        return QueryResult[YugiohSet](
            results=[orm_to_model(orm_model) for orm_model in results],
            total=total,
        )

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
