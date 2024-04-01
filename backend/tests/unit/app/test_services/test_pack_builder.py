from unittest.mock import Mock
import uuid

import pytest

from app.services.exceptions.set_exceptions import SetNotFound
from app.services import PackBuilder, GachaService
from app.repository import SetRepository, CardRepository
from app.models import Pack, YugiohCard


@pytest.fixture
def gacha_service() -> GachaService:
    return Mock(spec=GachaService)


@pytest.fixture
def set_repository() -> SetRepository:
    return Mock(spec=SetRepository)


@pytest.fixture
def card_repository():
    return Mock(spec=CardRepository)


@pytest.fixture
def sut(
    gacha_service: GachaService,
    set_repository: SetRepository,
    card_repository: CardRepository,
) -> PackBuilder:
    return PackBuilder(
        gacha_service=gacha_service,
        set_repository=set_repository,
        card_repository=card_repository,
    )


def create_card(name: str = "name"):
    return YugiohCard(
        id=uuid.uuid4(),
        name=name,
        type="type",
        description="desc",
        archetype="archie",
        race="elven warrior",
    )


def test_when_buildling_pack__looks_up_cards_using_card_repository(
    sut: PackBuilder, card_repository: CardRepository
):
    expected_cards = [create_card("bubby")]
    card_repository.get_cards_for_ids.return_value = expected_cards

    pack: Pack = sut.build_pack("id")

    assert pack.cards == expected_cards


def test_when_building_pack__looks_up_set_by_id_using_the_set_repository(
    sut: PackBuilder, card_repository: CardRepository, set_repository: SetRepository
):
    set_id = "id"
    card_repository.get_cards_for_ids.return_value = []

    sut.build_pack(set_id=set_id)

    set_repository.get_set_by_id.assert_called_with(set_id)


def test_when_building_pack__rolls_pack_using_gacha_service(
    sut: PackBuilder, card_repository: CardRepository, gacha_service: GachaService
):
    card_repository.get_cards_for_ids.return_value = []

    sut.build_pack("errob")

    gacha_service.roll_for_set.assert_called_once()


def test_when_raised_set_not_found__uses_set_id_given(
    sut: PackBuilder, card_repository: CardRepository, set_repository: SetRepository
):
    card_repository.get_cards_for_ids.return_value = []
    set_repository.get_set_by_id.return_value = None
    set_id = "dne"

    with pytest.raises(SetNotFound) as err:
        sut.build_pack(set_id)

    assert err.value.set_id == set_id


def test_when_set_repository_returns_none__raise_set_not_found(
    sut: PackBuilder, card_repository: CardRepository, set_repository: SetRepository
):
    card_repository.get_cards_for_ids.return_value = []
    set_repository.get_set_by_id.return_value = None

    with pytest.raises(SetNotFound):
        sut.build_pack("dne")
