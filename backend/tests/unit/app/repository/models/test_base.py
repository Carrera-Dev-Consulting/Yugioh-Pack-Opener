from sqlalchemy import Column, Integer, MetaData, String
from app.repository.models.base import BaseSQLModel

TABLE_NAME = "__example"


def remove_model(model):
    metadata: MetaData = BaseSQLModel.metadata
    metadata.remove(model.__table__)


def test_repr_for_model__works_on_model_with_single_column():
    class BasicModel(BaseSQLModel):
        __tablename__ = TABLE_NAME
        id: int = Column(Integer, primary_key=True, autoincrement=True)

    value = BasicModel(id=1)
    expected = "BasicModel(id=1)"
    actual = repr(value)
    remove_model(BasicModel)

    assert actual == expected


def test_repr_for_model__works_on_model_with_single_column_string():
    class BasicModel(BaseSQLModel):
        __tablename__ = TABLE_NAME
        id: str = Column(String, primary_key=True)

    value = BasicModel(id="1")
    expected = "BasicModel(id='1')"
    actual = repr(value)

    remove_model(BasicModel)

    assert actual == expected


def test_repr_for_model__when_building_string_for_model_with_multiple_columns__renders_all_columns():
    class BasicModel(BaseSQLModel):
        __tablename__ = TABLE_NAME
        id: str = Column(String, primary_key=True)
        other: int = Column(Integer, nullable=True)

    value = BasicModel(id="1", other=None)
    expected = "BasicModel(id='1', other=None)"
    actual = repr(value)

    remove_model(BasicModel)

    assert actual == expected
