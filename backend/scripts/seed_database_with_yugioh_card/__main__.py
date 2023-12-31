from contextlib import contextmanager
import datetime
import click
import os

from .db_layer import DBLayer
from .ygopro_api import YGOProAPIHandler


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
@click.option("--db-url", type=str, required=True)
@click.option("--cache-directory", default="api-responses")
@click.option("--card-json-images-directory", default="cards")
@click.option("--set-images-directory", default="sets")
@timer("Finished with main")
def main(
    db_url: str,
    cache_directory: str,
    card_json_images_directory: str,
    set_images_directory: str,
):
    cache_directory = f"cached/{cache_directory}"
    card_json_images_directory = f"cached/{card_json_images_directory}"
    set_images_directory = f"cached/{set_images_directory}"
    ensure_directory("cached")
    ensure_directory(cache_directory)
    ensure_directory(card_json_images_directory)
    ensure_directory(set_images_directory)

    api_handler = YGOProAPIHandler(cache_directory)
    # db_layer = DBLayer(db_url)
    card_sets = api_handler.get_sets()
    for card_set in card_sets:
        api_handler.save_set_images(card_set, set_images_directory)

    # db_layer.save_sets_in_database(card_sets)

    cards = api_handler.get_cards()
    for card in cards:
        api_handler.save_card_images(card, card_json_images_directory)
    # db_layer.save_cards_in_database(cards)


if __name__ == "__main__":
    main()
