from tempfile import TemporaryDirectory
import pytest
from scripts.seed_database_with_yugioh_card.ygopro_api import YGOProAPIHandler


@pytest.fixture()
def temp_dir():
    with TemporaryDirectory() as dir:
        yield dir


def test_when_calling_endpoint_twice__uses_cached_response(temp_dir):
    path = "https://google.com/"
    local_path = "google.html"
    handler = YGOProAPIHandler(temp_dir)

    handler._request_stream_to_file(path, local_path)

    assert handler.cacher.exists(local_path), "Not in cacher"

    handler._request_stream_to_file(path, local_path)
