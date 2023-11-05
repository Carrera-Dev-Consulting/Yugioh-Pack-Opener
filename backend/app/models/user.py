from .base import Base


class User(Base):
    username: str
    email: str | None = None
    meta: dict
