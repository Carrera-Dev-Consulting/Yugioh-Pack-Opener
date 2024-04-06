from datetime import date
import pytest
from sqlalchemy import Engine
from scripts.seed_database_with_yugioh_card.db_layer import DBLayer
from scripts.seed_database_with_yugioh_card.ygopro_api import YGoProSet


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
    return YGoProSet(
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
