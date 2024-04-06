from sqlalchemy.orm import declarative_base

BaseSQLModel = declarative_base()


def base_model_str(self) -> str:
    set_values = ",".join(f"{key}={getattr(self, key)}" for key in self.__columns__)
    return f"{type(self)}({set_values})"


BaseSQLModel.__repr__ = base_model_str
