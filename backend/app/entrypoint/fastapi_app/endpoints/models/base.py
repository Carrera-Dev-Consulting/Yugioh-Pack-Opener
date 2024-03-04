from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        frozen = True
