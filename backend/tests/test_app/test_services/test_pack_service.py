from unittest.mock import Mock

import pytest

from app.models import PackRequest, Pack
from app.services.pack_service import PackService
from app.services.pack_builder import PackBuilder


@pytest.fixture
def pack_builder() -> PackBuilder:
    return Mock(spec=PackBuilder)


@pytest.fixture
def sut(pack_builder) -> PackService:
    return PackService(pack_builder=pack_builder)


def test_when_given_request_for_ten_packs__calls_builder_ten_times(
    sut: PackService, pack_builder: PackBuilder
):
    total_packs = 10
    pack_builder.build_pack.return_value = Pack(cards=[])
    request = PackRequest(pack_id="pack-id", total_desired=total_packs)

    sut.open_packs([request])

    assert pack_builder.build_pack.call_count == total_packs


def test_when_given_no_request_items__returns_empty_array(
    sut: PackService, pack_builder: PackBuilder
):
    res = sut.open_packs([])

    assert res == []
