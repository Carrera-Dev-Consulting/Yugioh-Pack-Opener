from contextlib import contextmanager
from datetime import date
from enum import Enum
from logging import getLogger
import time
import json
import os
from typing import IO, Any, Callable, Generator


import requests
from pydantic import BaseModel, Field, field_validator

logger = getLogger(__name__)


class YGOProSet(BaseModel):
    set_name: str
    set_code: str
    num_of_cards: int
    tcg_date: date | None = None
    set_image: str | None = None

    @field_validator("tcg_date", mode="before")
    @classmethod
    def tcg_date_validator(cls, value: str):
        if value == "0000-00-00":
            return None
        return value


class YGOProSetReference(BaseModel):
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


class YGOProLinkMarker(str, Enum):
    Left = "Left"
    Right = "Right"
    Top = "Top"
    TopLeft = "Top-Left"
    TopRight = "Top-Right"
    Bottom = "Bottom"
    BottomLeft = "Bottom-Left"
    BottomRight = "Bottom-Right"


class YGOProFormat(str, Enum):
    BanGoat = "ban_goat"
    BanOCG = "ban_ocg"
    BanTCG = "ban_tcg"


class YGOProBanLevel(str, Enum):
    Limited = "Limited"
    SemiLimited = "Semi-Limited"
    Banned = "Banned"


class YGOProCard(BaseModel):
    id: int
    name: str
    type: str
    frameType: str
    desc: str
    scale: int | None = None
    defense: int | None = Field(
        None, alias="def"
    )  # because def is a reserved word need to alias it
    attack: int | None = Field(
        None, alias="atk"
    )  # wanted it to match def since this is the inverse property on monsters
    banlist_info: dict[YGOProFormat, YGOProBanLevel] | None = None
    archtype: str | None = None
    attribute: str | None = None
    level: int | None = None
    race: str | None = None
    archetype: str | None = None
    linkmarkers: list[YGOProLinkMarker] | None = None
    linkval: int | None = None
    card_sets: list[YGOProSetReference] = []
    card_images: list[YGOProCardImage] = []
    card_prices: list[YGOProCardPrice] = []


def null_transform(response_body):
    return response_body


class DirectoryCacher:
    def __init__(self, directory: str) -> None:
        self.directory = directory
        self.computed_entries: dict[str, Any] = {}

    def _path_for_entry(self, cache_entry: str):
        if cache_entry not in self.computed_entries:
            self.computed_entries[cache_entry] = f"{self.directory}/{cache_entry}"
        return self.computed_entries[cache_entry]

    @contextmanager
    def open_write_buffer(
        self, cache_entry, binary=False
    ) -> Generator[IO[Any], Any, None]:
        flags = ["w"]
        if binary:
            flags.append("b")
        file_flags = "".join(flags)
        file_path = self._path_for_entry(cache_entry)
        logger.info(f"Opening file: {file_path} with Flags: {file_flags}")
        with open(file_path, file_flags) as fp:
            yield fp

    def exists(self, cache_entry: str) -> bool:
        return os.path.exists(self._path_for_entry(cache_entry))

    def read(self, cache_entry: str, as_json=False) -> str | dict | list:
        if not self.exists(cache_entry):
            return "{}" if as_json else {}
        print(f"Opening file: {self._path_for_entry(cache_entry)}")
        with open(self._path_for_entry(cache_entry), "r") as fp:
            if as_json:
                return json.load(fp)
            else:
                return fp.read()


class YGOProAPIHandler:
    def __init__(
        self,
        cache_directory: str = "api-responses",
        cacher=None,
        requests=requests,
        sleep=time.sleep,
    ) -> None:
        self.requests_made = 0
        self.cacher = cacher or DirectoryCacher(cache_directory)
        self.requests = requests
        self.sleep = sleep

    def _make_request(self, path: str, **kwargs):
        if self.requests_made < 4:
            response = self.requests.get(path, **kwargs)
            self.requests_made += 1
            return response
        else:
            print("Sleeping for a bit to not overload YGOPro API...")
            self.sleep(1.1)  # this is set by the api not us
            self.requests_made = 0
            return self._make_request(path, **kwargs)

    def _request_stream_to_file(self, url, localpath):
        if not url:
            return

        if os.path.exists(localpath):
            print("File already exists skipping...")
            return

        with self._make_request(url, stream=True) as response:
            with self.cacher.open_write_buffer(localpath, binary=True) as fp:
                for chunk in response.iter_content(255):
                    fp.write(chunk)

    def _get_or_cache_response(
        self,
        cache_file_name: str,
        api_path: str,
        transform_response: Callable[[dict | list], dict | list] = null_transform,
    ) -> list | dict | str:
        if self.cacher.exists(cache_file_name):
            return self.cacher.read(cache_file_name, as_json=True)

        response = self._make_request(api_path)
        parsed = transform_response(response.json())
        with self.cacher.open_write_buffer(cache_file_name, binary=False) as fp:
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

    def get_sets(self) -> list[YGOProSet]:
        raw_response = self._get_or_cache_response(
            "card_sets.json",
            "https://db.ygoprodeck.com/api/v7/cardsets.php",
        )
        return [YGOProSet.model_validate(card_set) for card_set in raw_response]

    def save_set_images(self, card_set: YGOProSet, directory: str):
        self._request_stream_to_file(
            card_set.set_image, f"{directory}/{card_set.set_code}.jpg"
        )
