from sqlalchemy.orm import Mapped
from database import Base
from custom_types import str_100, intpk


class Ingredients(Base):
    __tablename__ = "ingredients"
    id: Mapped[intpk]
    title: Mapped[str_100]
    type: Mapped[str_100]
    cost: Mapped[float]
