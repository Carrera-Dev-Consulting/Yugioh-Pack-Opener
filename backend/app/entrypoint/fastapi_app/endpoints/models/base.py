from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    model_config = ConfigDict(frozen=True)
