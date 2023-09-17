from enum import Enum
from typing import Any
from uuid import UUID

from pydantic import field_validator
from .base import Base


class YugiohCardType(str, Enum):
    EffectMonster = "Effect Monster"
    TunerMonster = "Tuner Monster"
    SynchroPendulumEffectMonster = "Synchro Pendulum Effect Monster"
    PendulumEffectMonster = "Pendulum Effect Monster"
    GeminiMonster = "Gemini Monster"
    NormalTunerMonster = "Normal Tuner Monster"
    PendulumFlipEffectMonster = "Pendulum Flip Effect Monster"
    SynchroMonster = "Synchro Monster"
    ToonMonster = "Toon Monster"
    FusionMonster = "Fusion Monster"
    PendulumEffectFusionMonster = "Pendulum Effect Fusion Monster"
    SpellCard = "Spell Card"
    XYZMonster = "XYZ Monster"
    PendulumNormalMonster = "Pendulum Normal Monster"
    SynchroTunerMonster = "Synchro Tuner Monster"
    Token = "Token"
    Skill = "Skill Card"
    RitualMonster = "Ritual Monster"
    RitualEffectMonster = "Ritual Effect Monster"
    SpiritMonster = "Spirit Monster"
    FlipEffectMonster = "Flip Effect Monster"
    PendulumTunerEffectMonster = "Pendulum Tuner Effect Monster"
    PendulumEffectRitualMonster = "Pendulum Effect Ritual Monster"
    LinkMonster = "Link Monster"
    XYZPendulumEffectMonster = "XYZ Pendulum Effect Monster"
    UnionEffectMonster = "Union Effect Monster"
    TrapCard = "Trap Card"
    NormalMonster = "Normal Monster"


class YugiohSetInfo(Base):
    set_id: str
    rarity: str
    rarity_code: str
    price: str | None


class YugiohCard(Base):
    id: UUID
    external_id: Any | None = None
    name: str
    type: YugiohCardType | None
    description: str
    archetype: str | None
    race: str | None
    sets: list[YugiohSetInfo] = []

    @field_validator("type", mode="before")
    def _parse_type(cls, _type: str | None):
        if _type is None:
            return _type
        try:
            return YugiohCardType(_type)
        except ValueError:
            # currently unmapped so mark it as none instead. consider adding specific field for unknown
            return None
