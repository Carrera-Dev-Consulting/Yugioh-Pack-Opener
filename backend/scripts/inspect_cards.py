from .seed_database_with_yugioh_card.ygopro_api import YGOProAPIHandler, YGOProCard
from operator import attrgetter


def get_length_of_description(card: YGOProCard):
    return len(card.desc)


def main():
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


if __name__ == "__main__":
    main()
