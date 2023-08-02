from contextlib import contextmanager
from typing import Iterable, TypeVar
import sqlalchemy
import sqlalchemy.orm

from app.repository.models import YugiohCard, YugiohSet, YugiohCardSetAssociation
from .ygopro_api import YGOProCard, YGOProSet


@contextmanager
def scoped_session(connection_string):
    engine = sqlalchemy.create_engine(connection_string)
    with sqlalchemy.orm.Session(engine) as session:
        yield session


def map_ygopro_to_orm(card: YGOProCard) -> YugiohCard:
    return YugiohCard(
        external_id=card.id,
        name=card.name,
        type=card.type,
        description=card.desc,
        archetype=card.archetype,
        race=card.race,
    )


T = TypeVar("T")


def iter_chunk_list(items: list[T], chunk_size: int) -> Iterable[list[T]]:
    return (
        items[index : index + chunk_size] for index in range(0, len(items), chunk_size)
    )


def create_card_set_association(
    card_set: YGOProSet, orm_card: YugiohCard, orm_set: YugiohSet
) -> YugiohCardSetAssociation:
    return YugiohCardSetAssociation(
        card_id=orm_card.id,
        set_id=orm_set.id,
        rarity=card_set.set_rarity,
        rarity_code=card_set.set_rarity_code,
        price=card_set.set_price,
    )


def limit_cards_not_in_db(
    cards: list[YGOProCard], session: sqlalchemy.orm.Session
) -> list[YGOProCard]:
    card_ids = [card.id for card in cards]
    stored_ids = {
        record.external_id
        for record in session.query(YugiohCard.external_id)
        .filter(YugiohCard.external_id.in_(card_ids))
        .all()
    }
    return [card for card in cards if card.id not in stored_ids]


def limit_sets_to_not_in_db(
    defined_sets: list[dict],
    orm_mapped: dict[str, YugiohSet],
    session: sqlalchemy.orm.Session,
):
    set_ids = [defined_set["set_id"] for defined_set in defined_sets]
    existing_records: list[YugiohSet] = (
        session.query(YugiohSet).filter(YugiohSet.set_id.in_(set_ids)).all()
    )
    orm_mapped.update((record.set_id, record) for record in existing_records)
    return [
        defined_set
        for defined_set in defined_sets
        if defined_set["set_id"] not in orm_mapped
    ]


def save_cards_in_database(cards: list[YGOProCard], connection_string):
    with scoped_session(connection_string) as session:
        unique_sets = [
            *{
                {
                    "name": card_set.set_name,
                    "set_id": card_set.set_code,
                }
                for card in cards
                for card_set in card.card_sets
            }
        ]
        cards = limit_cards_not_in_db(cards, session)
        orm_cards = {}
        orm_sets = {}
        unique_sets = limit_sets_to_not_in_db(unique_sets, orm_sets, session)
        # use set for uniqueness then put it into a list for chunking

        for set_chunk in iter_chunk_list(unique_sets, 50):
            for card_set in set_chunk:
                orm_set = YugiohSet(**card_set)
                session.add(orm_set)
                orm_sets[orm_set.set_id] = orm_set
            session.commit()

        for cards_chunk in iter_chunk_list(cards, 50):
            for card in cards_chunk:
                orm_card = map_ygopro_to_orm(card)
                session.add(orm_card)
                orm_cards[orm_card.external_id] = orm_card
            session.commit()

            for card in cards_chunk:
                orm_card = orm_cards[card.id]
                for card_set in card.card_sets:
                    orm_set = orm_sets[card_set.set_code]
                    association = create_card_set_association(
                        card_set, orm_card, orm_set
                    )
                    session.add(association)
            session.commit()
