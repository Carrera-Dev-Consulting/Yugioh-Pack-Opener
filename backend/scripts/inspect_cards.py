from typing import Iterable
from .seed_database_with_yugioh_card.ygopro_api import YGOProAPIHandler, YGOProCard
import json


def get_length_of_description(card: YGOProCard):
    return len(card.desc)


def print_longest_card():
    handler = YGOProAPIHandler()
    longest_desc = max(handler.get_cards(), key=get_length_of_description)
    print(
        "Card",
        longest_desc.name,
        f"({longest_desc.id})",
        "Has longest description",
        len(longest_desc.desc),
    )
    print(longest_desc.desc)


def save_into_json_output_all_kinds_of_cards():
    cards = get_cards()
    unique_cards = {}

    for card in cards:
        card_type = card["type"]

        if card_type in ["Spell Card", "Trap Card"]:
            sub_type = card["race"]
            card_type = f"{card_type}{sub_type}"

        if card_type not in unique_cards:
            unique_cards[card_type] = card

    print(len(unique_cards), "Total unique cards")
    with open("output.json", "w") as fp:
        json.dump(list(unique_cards.values()), fp)


def print_all_fields_on_each_card():
    cards = get_cards()
    all_field_names = {name for card in cards for name in card.keys()}
    for field in all_field_names:
        print(field)


def get_cards() -> list[dict]:
    with open("api-responses/cards.json", "r") as fp:
        return json.load(fp)


def get_link_cards() -> Iterable[dict]:
    cards = get_cards()
    for card in cards:
        if card["type"] == "Link Monster":
            yield card


def print_all_linkmarkers():
    link_cards = get_link_cards()
    link_markers = {marker for card in link_cards for marker in card["linkmarkers"]}
    print(link_markers)


def print_lowest_link_value():
    min_val = 1000000
    max_val = -1
    for card in get_link_cards():
        min_val = min(min_val, card["linkval"])
        max_val = max(max_val, card["linkval"])
    print("min", min_val, "max", max_val)


def print_keys_for_all_link_monsters():
    all_properties = {prop for card in get_link_cards() for prop in card.keys()}
    print(all_properties)


def print_cards_properties_with_banlist_info():
    cards = get_cards()
    properties = set()
    for card in cards:
        if "banlist_info" in card:
            properties.update(card["banlist_info"].keys())
    for property in properties:
        print(property)


def main():
    print_longest_card()
    # save_into_json_output_all_kinds_of_cards()
    # print_all_fields_on_each_card()
    # print_all_linkmarkers()
    # print_lowest_link_value()
    # print_keys_for_all_link_monsters()
    # print_cards_properties_with_banlist_info()


if __name__ == "__main__":
    main()
