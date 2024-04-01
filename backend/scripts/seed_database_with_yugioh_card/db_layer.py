from contextlib import contextmanager
import functools
from typing import Iterable, TypeVar
import sqlalchemy
import sqlalchemy.orm

from app.repository.models import YugiohCardORM, YugiohSetORM, YugiohCardSetAssociation
from .ygopro_api import YGOProCard, YGOProSetReference, YGoProSet

T = TypeVar("T")


def iter_chunk_list(items: list[T], chunk_size: int) -> Iterable[list[T]]:
    return (
        items[index : index + chunk_size] for index in range(0, len(items), chunk_size)
    )


defined_columns = {m.key for m in YugiohCardORM.__table__.columns}


@functools.singledispatch
def map_ygopro_to_orm(ygopro_model):
    raise NotImplemented(
        f"Not mapping for ygopro to orm model for type: {type(ygopro_model)}"
    )


@map_ygopro_to_orm.register
def _(card: YGOProCard) -> YugiohCardORM:
    data = {"external_id": card.id, **card.model_dump()}
    not_applicable_keys = [key for key in data if key not in defined_columns]

    for key in not_applicable_keys:
        data.pop(key, None)

    return YugiohCardORM(**data)


@map_ygopro_to_orm.register
def _(card_set: YGoProSet) -> YugiohSetORM:
    return YugiohSetORM(
        set_id=card_set.set_code,
        name=card_set.set_name,
        release_date=card_set.tcg_date,
        card_count=card_set.num_of_cards,
    )


def create_card_set_association(
    card_set: YGOProSetReference, orm_card: YugiohCardORM, orm_set: YugiohSetORM
) -> YugiohCardSetAssociation:
    return YugiohCardSetAssociation(
        card=orm_card,
        set=orm_set,
        rarity=card_set.set_rarity,
        rarity_code=card_set.set_rarity_code,
        price=card_set.set_price,
    )


class DBLayer:
    def __init__(self, engine: sqlalchemy.engine.Engine):
        self.engine = engine

    @classmethod
    def from_connection_string(cls, connection_string: str):
        return cls(sqlalchemy.create_engine(connection_string))

    @contextmanager
    def scoped_session(self):
        with sqlalchemy.orm.Session(self.engine) as session:
            yield session

    def save_cards_in_database(self, cards: list[YGOProCard]):
        with self.scoped_session() as session:
            cards = limit_cards_not_in_db(cards, session)
            orm_cards: dict[str, YugiohCardORM] = {}
            orm_sets = get_sets_from_database(session)

            for cards_chunk in iter_chunk_list(cards, 50):
                for card in cards_chunk:
                    orm_card = map_ygopro_to_orm(card)
                    session.add(orm_card)
                    orm_cards[orm_card.external_id] = orm_card
                session.commit()
                associations: list[
                    tuple[YugiohCardORM, YugiohSetORM, YGOProSetReference]
                ] = []
                for card in cards_chunk:
                    orm_card = orm_cards[card.id]
                    for card_set in card.card_sets:
                        orm_set = orm_sets.get(card_set.set_code)
                        if orm_set:
                            create_card_set_association(
                                card_set=card_set, orm_card=orm_card, orm_set=orm_set
                            )
                session.commit()

    def save_sets_in_database(self, card_sets: list[YGoProSet]):
        index_by_id = {card_set.set_code: card_set for card_set in card_sets}
        with self.scoped_session() as session:
            # get existing sets in the db
            existing = get_sets_from_database(session)
            # subtract the ones we already track from the cards we just see
            for key in existing:
                index_by_id.pop(key, None)
            # save the new records
            save_sets_in_db(session, index_by_id.values())


def limit_cards_not_in_db(
    cards: list[YGOProCard], session: sqlalchemy.orm.Session
) -> list[YGOProCard]:
    card_ids = [card.id for card in cards]
    stored_ids = {
        record.external_id
        for record in session.query(YugiohCardORM.external_id)
        .filter(YugiohCardORM.external_id.in_(card_ids))
        .all()
    }
    return [card for card in cards if card.id not in stored_ids]


def limit_card_sets_not_in_db(
    card_sets: list[YGoProSet], session: sqlalchemy.orm.Session
):
    set_ids = [card_set.set_code for card_set in card_sets]
    stored_ids = {
        record.external_id
        for record in session.query(YugiohSetORM.set_id)
        .filter(YugiohSetORM.set_id.in_(set_ids))
        .all()
    }
    return [card_set for card_set in card_sets if card_set.set_code not in stored_ids]


def get_sets_from_database(session: sqlalchemy.orm.Session) -> dict[str, YugiohSetORM]:
    sets: list[YugiohSetORM] = session.query(YugiohSetORM).all()
    return {yugioh_set.set_id: yugioh_set for yugioh_set in sets}


def save_sets_in_db(session: sqlalchemy.orm.Session, card_sets: list[YGoProSet]):
    for card_set in card_sets:
        db_model: YugiohSetORM = map_ygopro_to_orm(card_set)
        session.add(db_model)
    session.commit()
