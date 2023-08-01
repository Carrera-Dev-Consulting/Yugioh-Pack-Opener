from app.models.base import Base


class TCGCardImage(Base):
    image_url: str
    image_small_url: str
    image_cropped_url: str

class TCGSetReference(Base):
    name: str
    set_id: str
    rarity: str


class TCGCard(Base):
    metadata: any
    id: str
    game: str
    name: str
    description: str
    images: list[TCGCardImage]
    sets: list[TCGSetReference]
