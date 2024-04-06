from sqlalchemy.orm import declarative_base

BaseSQLModel = declarative_base()


def base_model_str(self) -> str:
    columns = [column.name for column in self.__table__.columns]
    set_values = ", ".join(f"{key}={getattr(self, key)!r}" for key in columns)
    return f"{type(self).__name__}({set_values})"


BaseSQLModel.__repr__ = base_model_str
