from datetime import date
import pytest
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session, joinedload
from app.repository.models import YugiohCardORM
from scripts.seed_database_with_yugioh_card.db_layer import DBLayer
from scripts.seed_database_with_yugioh_card.ygopro_api import (
    YGOProCard,
    YGOProSetReference,
    YGOProSet,
)


@pytest.fixture(scope="function")
def sut(database_session: Engine):
    return DBLayer(database_session)


def test_db_layer__when_looking_up_sets_and_database_is_empty__returns_nothing(sut):
    existing_sets = sut.get_sets_from_database()

    assert not existing_sets, "There are somehow sets before I added my seed hehe"


def create_ygo_pro_set(
    num_of_cards: int = 1,
    set_code: str = "code",
    set_image: str = "image",
    set_name: str = "name",
    tcg_date: date = None,
):
    return YGOProSet(
        num_of_cards=num_of_cards,
        set_code=set_code,
        set_image=set_image,
        set_name=set_name,
        tcg_date=tcg_date or date.today(),
    )


def test_db_layer__when_looking_up_sets_after_saving_them__returns_added_sets(sut):

    sets = [create_ygo_pro_set(set_code="beyblade")]

    sut.save_sets_in_database(sets)

    existing_sets = sut.get_sets_from_database()

    assert (
        existing_sets
    ), "The set was never saved in the database like it should have been"
    assert "beyblade" in existing_sets, "Expected set to be referened by set_code"


def create_ygo_pro_card(
    id: int = 1,
    name: str = "card",
    type: str = "monster",
    frameType: str = "frame",
    desc: str = "desc",
):
    return YGOProCard(id=id, name=name, type=type, frameType=frameType, desc=desc)


def test_db_layer__when_adding_cards__associates_to_existing_sets(
    sut: DBLayer, database_session: Engine
):
    sut.save_sets_in_database([create_ygo_pro_set(set_code="code")])
    card = create_ygo_pro_card(id=1)
    card.card_sets.append(
        YGOProSetReference(
            set_code="code",
            set_name="denims",
            set_price="$1.00",
            set_rarity="rare",
            set_rarity_code="RARE",
        )
    )

    sut.save_cards_in_database([card])

    with Session(database_session) as session:
        result = (
            session.execute(
                select(YugiohCardORM)
                .options(joinedload(YugiohCardORM.sets))
                .where(YugiohCardORM.external_id == 1)
            )
            .unique()
            .scalars() 
            .all()
        )
    db_card = result[0]
    assert db_card.sets, "Did not load sets correctly from the database after saving"
