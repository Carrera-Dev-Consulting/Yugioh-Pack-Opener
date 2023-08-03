from contextlib import contextmanager
from typing import Iterable, TypeVar
import sqlalchemy
import sqlalchemy.orm

from app.repository.models import YugiohCard, YugiohSet, YugiohCardSetAssociation
from .ygopro_api import YGOProCard, YGoProSetReference, YGoProSet

T = TypeVar("T")


def iter_chunk_list(items: list[T], chunk_size: int) -> Iterable[list[T]]:
    return (
        items[index : index + chunk_size] for index in range(0, len(items), chunk_size)
    )


def map_ygopro_to_orm(card: YGOProCard) -> YugiohCard:
    return YugiohCard(
        external_id=card.id,
        name=card.name,
        type=card.type,
        description=card.desc,
        archetype=card.archetype,
        race=card.race,
    )


def create_card_set_association(
    card_set: YGoProSetReference, orm_card: YugiohCard, orm_set: YugiohSet
) -> YugiohCardSetAssociation:
    return YugiohCardSetAssociation(
        card_id=orm_card.id,
        set_id=orm_set.id,
        rarity=card_set.set_rarity,
        rarity_code=card_set.set_rarity_code,
        price=card_set.set_price,
    )


class DBLayer:
    def __init__(self, connection_string: str):
        self.engine = sqlalchemy.create_engine(connection_string)

    @contextmanager
    def scoped_session(self):
        with sqlalchemy.orm.Session(self.engine) as session:
            yield session

    def save_cards_in_database(self, cards: list[YGOProCard]):
        with self.scoped_session() as session:
            cards = limit_cards_not_in_db(cards, session)
            orm_cards: dict[str, YugiohCard] = {}
            orm_sets = get_sets_from_database(session)

            for cards_chunk in iter_chunk_list(cards, 50):
                for card in cards_chunk:
                    orm_card = map_ygopro_to_orm(card)
                    session.add(orm_card)
                    orm_cards[orm_card.external_id] = orm_card
                session.commit()

                for card in cards_chunk:
                    orm_card = orm_cards[card.id]
                    for card_set in card.card_sets:
                        orm_set = orm_sets.get(card_set.set_code)
                        if orm_set:
                            association = create_card_set_association(
                                card_set, orm_card, orm_set
                            )
                            session.add(association)
                session.commit()

    def save_sets_in_database(self, card_sets: list[YGoProSet]):
        with self.scoped_session() as session:
            pass


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


def limit_card_sets_not_in_db(
    card_sets: list[YGoProSet], session: sqlalchemy.orm.Session
):
    set_ids = [card_set.set_code for card_set in card_sets]
    stored_ids = {
        record.external_id
        for record in session.query(YugiohSet.set_id)
        .filter(YugiohSet.set_id.in_(set_ids))
        .all()
    }
    return [card_set for card_set in card_sets if card_set.set_code not in stored_ids]


def get_sets_from_database(session: sqlalchemy.orm.Session) -> dict[str, YugiohSet]:
    sets: list[YugiohSet] = session.query(YugiohSet).all()
    return {yugioh_set.set_id: yugioh_set for yugioh_set in sets}
