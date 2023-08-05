from .base import Base
from .pack import Pack


class PackRequestResult(Base):
    cards_pulled: list[Pack]
