from contextlib import contextmanager
import functools
from logging import getLogger
from typing import Iterable, TypeVar, cast
import sqlalchemy
import sqlalchemy.orm

from app.repository.models import YugiohCardORM, YugiohSetORM, YugiohCardSetAssociation
from .ygopro_api import YGOProCard, YGOProSetReference, YGOProSet

T = TypeVar("T")

logger = getLogger(__name__)


def iter_chunk_list(items: list[T], chunk_size: int) -> Iterable[list[T]]:
    return (
        items[index : index + chunk_size] for index in range(0, len(items), chunk_size)
    )


defined_columns = {m.key for m in YugiohCardORM.__table__.columns}


@functools.singledispatch
def map_ygopro_to_orm(ygopro_model):
    raise ValueError(
        f"Not mapping for ygopro to orm model for type: {type(ygopro_model)}"
    )


@map_ygopro_to_orm.register
def _(card: YGOProCard) -> YugiohCardORM:
    data = card.model_dump()
    not_applicable_keys = [key for key in data if key not in defined_columns]

    for key in not_applicable_keys:
        data.pop(key, None)

    data["description"] = card.desc
    data["link_value"] = card.linkval
    data["links"] = ",".join(card.linkmarkers) if card.linkmarkers else None
    data["external_id"] = card.id
    data.pop("id", None)  # need to let the orm handle this

    return YugiohCardORM(**data)


@map_ygopro_to_orm.register
def _(card_set: YGOProSet) -> YugiohSetORM:
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
        self.session = None

    @classmethod
    def from_connection_string(cls, connection_string: str):
        return cls(sqlalchemy.create_engine(connection_string))

    @contextmanager
    def scoped_session(self):
        if self.session is not None:
            yield self.session
        else:
            with sqlalchemy.orm.Session(self.engine) as session:
                self.session = session
                yield session
                self.session = None

    def save_cards_in_database(self, cards: list[YGOProCard]):
        with self.scoped_session() as session:
            cards = limit_cards_not_in_db(cards, session)
            orm_cards: dict[str, YugiohCardORM] = {}
            orm_sets = self.get_sets_from_database()
            unique_cache = set()
            logger.info(f"Found existing sets: {orm_sets}")

            for cards_chunk in iter_chunk_list(cards, 50):
                for card in cards_chunk:
                    orm_card = map_ygopro_to_orm(card)
                    session.add(orm_card)
                    orm_cards[orm_card.external_id] = orm_card
                session.commit()
                for card in cards_chunk:
                    orm_card = orm_cards[card.id]
                    for card_set in card.card_sets:
                        code = card_set.set_code
                        if "-" in code:
                            logger.debug(f"Splitting code: {code}")
                            code = code.split("-")[0]
                        orm_set = orm_sets.get(code)

                        logger.debug(f"Found Set={orm_set} for code={code}")
                        if orm_set:
                            if (orm_card.id, orm_set.id) in unique_cache:
                                logger.warning("Duplicate entry for set")
                                continue
                            unique_cache.add((orm_card.id, orm_set.id))
                            logger.debug("Creating Association")
                            association = create_card_set_association(
                                card_set=card_set, orm_card=orm_card, orm_set=orm_set
                            )
                            session.add(association)
                session.commit()

    def save_sets_in_database(self, card_sets: list[YGOProSet]):
        index_by_id = {card_set.set_code: card_set for card_set in card_sets}
        with self.scoped_session() as session:
            # get existing sets in the db
            existing = self.get_sets_from_database()
            # subtract the ones we already track from the cards we just see
            for key in existing:
                index_by_id.pop(key, None)
            # save the new records
            save_sets_in_db(session, index_by_id.values())

    def get_sets_from_database(self) -> dict[str, YugiohSetORM]:
        with self.scoped_session() as session:
            sets: list[YugiohSetORM] = session.query(YugiohSetORM).all()
        return {cast(str, yugioh_set.set_id): yugioh_set for yugioh_set in sets}


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
    card_sets: list[YGOProSet], session: sqlalchemy.orm.Session
):
    set_ids = [card_set.set_code for card_set in card_sets]
    stored_ids = {
        record.external_id
        for record in session.query(YugiohSetORM.set_id)
        .filter(YugiohSetORM.set_id.in_(set_ids))
        .all()
    }
    return [card_set for card_set in card_sets if card_set.set_code not in stored_ids]


def save_sets_in_db(session: sqlalchemy.orm.Session, card_sets: Iterable[YGOProSet]):
    for card_set in card_sets:
        db_model: YugiohSetORM = map_ygopro_to_orm(card_set)
        session.add(db_model)
    session.commit()
