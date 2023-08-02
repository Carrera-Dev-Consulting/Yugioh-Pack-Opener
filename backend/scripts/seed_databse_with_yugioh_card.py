import click
import os

from .db_layer import save_cards_in_database
from .ygopro_api import YGOProAPIHandler


@click.command()
@click.option("--db-url", type=str)
@click.option("--card-json-file", default="cards.json")
@click.option("--card-json-images-directory", default="cards")
def main(db_url: str, card_json_file: str, card_json_images_directory: str):
    if not os.path.exists(card_json_images_directory):
        os.mkdir(card_json_images_directory)
    api_handler = YGOProAPIHandler(card_json_file)
    cards = api_handler.get_cards()

    for card in cards:
        api_handler.save_card_images(card, card_json_images_directory)
    save_cards_in_database(cards)


if __name__ == "__main__":
    main()
