from datetime import date
import time
import json
import os
from typing import Callable


import requests
from pydantic import BaseModel


class YGoProSet(BaseModel):
    set_name: str
    set_code: str
    num_of_cards: int
    tcg_date: date | None = None
    set_image: str | None = None


class YGoProSetReference(BaseModel):
    set_name: str
    set_code: str
    set_rarity: str
    set_rarity_code: str
    set_price: str


class YGOProCardImage(BaseModel):
    id: int
    image_url: str
    image_url_small: str
    image_url_cropped: str


class YGOProCardPrice(BaseModel):
    cardmarket_price: str | None
    tcgplayer_price: str | None
    ebay_price: str | None
    amazon_price: str | None
    coolstuffinc_price: str | None


class YGOProCard(BaseModel):
    id: int
    name: str
    type: str
    frameType: str
    desc: str
    race: str | None = None
    archetype: str | None = None
    card_sets: list[YGoProSetReference] = []
    card_images: list[YGOProCardImage] = []
    card_prices: list[YGOProCardPrice] = []


def null_transform(response_body):
    return response_body


class YGOProAPIHandler:
    def __init__(self, cache_directory: str = "cards.json") -> None:
        self.requests_made = 0
        self.cache_directory = cache_directory

    def _make_request(self, path: str, **kwargs):
        if self.requests_made < 4:
            response = requests.get(path, **kwargs)
            self.requests_made += 1
            return response
        else:
            print("Sleeping for a bit to not overload YGOPro API...")
            time.sleep(1.1)
            self.requests_made = 0
            return self._make_request(path, **kwargs)

    def _request_stream_to_file(self, url, localpath):
        if not url:
            return

        if os.path.exists(localpath):
            print("File already exists skipping...")
            return

        with self._make_request(url, stream=True) as response:
            with open(localpath, "wb") as fp:
                for chunk in response.iter_content(255):
                    fp.write(chunk)

    def _get_or_cache_response(
        self,
        cache_file_name: str,
        api_path: str,
        transform_response: Callable[[dict | list], dict | list] = null_transform,
    ) -> list | dict:
        full_path = f"{self.cache_directory}/{cache_file_name}"
        if os.path.exists(full_path):
            with open(full_path, "r") as fp:
                return json.load(fp)

        response = self._make_request(api_path)
        parsed = transform_response(response.json())
        with open(full_path, "w") as fp:
            json.dump(parsed, fp)
        return parsed

    def get_cards(self):
        raw_response = self._get_or_cache_response(
            "cards.json",
            "https://db.ygoprodeck.com/api/v7/cardinfo.php",
            lambda v: v["data"],
        )

        return [YGOProCard.model_validate(card) for card in raw_response]

    def save_card_images(self, card: YGOProCard, directory: str):
        for image in card.card_images:
            self._request_stream_to_file(image.image_url, f"{directory}/{card.id}.jpg")
            self._request_stream_to_file(
                image.image_url_cropped, f"{directory}/{card.id}-cropped.jpg"
            )
            self._request_stream_to_file(
                image.image_url_small, f"{directory}/{card.id}-small.jpg"
            )

    def get_sets(self) -> list[YGoProSet]:
        raw_response = self._get_or_cache_response(
            "card_sets.json",
            "https://db.ygoprodeck.com/api/v7/cardsets.php",
        )
        return [YGoProSet.model_validate(card_set) for card_set in raw_response]

    def save_set_images(self, card_set: YGoProSet, directory: str):
        self._request_stream_to_file(
            card_set.set_image, f"{directory}/{card_set.set_code}.jpg"
        )
