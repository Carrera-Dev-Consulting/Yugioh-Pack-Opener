from typing import Iterable

from app.models import PackRequestResult, YugiohCard, YugiohCardType
from .base import ResultExporter

MAIN_DECK_TYPES = [
    YugiohCardType.EffectMonster,
    YugiohCardType.NormalMonster,
    YugiohCardType.FlipEffectMonster,
    YugiohCardType.GeminiMonster,
    YugiohCardType.PendulumEffectMonster,
    YugiohCardType.PendulumEffectRitualMonster,
    YugiohCardType.PendulumFlipEffectMonster,
    YugiohCardType.PendulumNormalMonster,
    YugiohCardType.PendulumTunerEffectMonster,
    YugiohCardType.ToonMonster,
    YugiohCardType.TunerMonster,
    YugiohCardType.NormalTunerMonster,
    YugiohCardType.RitualEffectMonster,
    YugiohCardType.RitualMonster,
    YugiohCardType.SpellCard,
    YugiohCardType.TrapCard,
    YugiohCardType.SpiritMonster,
    YugiohCardType.UnionEffectMonster,
]
EXTRA_DECK_TYPES = [
    YugiohCardType.FusionMonster,
    YugiohCardType.PendulumEffectFusionMonster,
    YugiohCardType.XYZMonster,
    YugiohCardType.XYZPendulumEffectMonster,
    YugiohCardType.SynchroMonster,
    YugiohCardType.SynchroPendulumEffectMonster,
    YugiohCardType.SynchroTunerMonster,
    YugiohCardType.LinkMonster,
]


class YDKResultExporter(ResultExporter):
    def _format_line(self, line: str):
        return f"{line}\n".encode(self.encoding)

    def export(self, pack_request_result: PackRequestResult) -> Iterable[bytes]:
        yield self._format_line(f"#created by {self.creator_name}")
        mains = []
        extra_deck = []
        for card in pack_request_result:
            if card.type in MAIN_DECK_TYPES:
                mains.append(card)
            elif card.type in EXTRA_DECK_TYPES:
                extra_deck.append()
        yield from self._format_group("#main", mains)
        yield from self._format_group("#extra", extra_deck)
        yield self._format_line("!side")

    def _format_group(self, header: str, cards: list[YugiohCard]):
        yield self._format_line(header)
        for card in cards:
            yield self._format_line(f"{card.external_id}")
