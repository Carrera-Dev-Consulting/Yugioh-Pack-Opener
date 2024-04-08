from contextlib import contextmanager
import datetime
from logging import getLogger
import click
import os

from .db_layer import DBLayer
from .ygopro_api import YGOProAPIHandler
from app.config import server_config
from app.services.logging import configure_logging

logger = getLogger(__name__)


def ensure_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)


@contextmanager
def timer(message: str):
    start_time = datetime.datetime.utcnow()
    yield
    end_time = datetime.datetime.utcnow()
    print(f"{message}: Total Execution Time {end_time - start_time}")


@click.command()
@click.option("--skip-db", type=bool, default=False, is_flag=True)
@click.option("-d", "--db-url", type=str, required=False)
@click.option("-c", "--cache-directory", default="api-responses")
@click.option("-i", "--card-json-images-directory", default="cards")
@click.option("-s", "--set-images-directory", default="sets")
@timer("Finished with main")
def main(
    db_url: str,
    skip_db: bool,
    cache_directory: str,
    card_json_images_directory: str,
    set_images_directory: str,
):
    configure_logging()
    if db_url is None:
        db_url = server_config().mysql_url
    ensure_directory("cached")
    ensure_directory(f"cached/{cache_directory}")
    ensure_directory(f"cached/{card_json_images_directory}")
    ensure_directory(f"cached/{set_images_directory}")

    api_handler = YGOProAPIHandler(f"cached")
    card_sets = api_handler.get_sets()
    for card_set in card_sets:
        api_handler.save_set_images(card_set, set_images_directory)

    cards = api_handler.get_cards()
    for card in cards:
        api_handler.save_card_images(card, card_json_images_directory)

    if skip_db:
        logger.info(f"Skipping Database insertion for url: {db_url}")
        return

    db_layer = DBLayer.from_connection_string(db_url)
    db_layer.save_sets_in_database(card_sets)
    db_layer.save_cards_in_database(cards)


if __name__ == "__main__":
    main()
