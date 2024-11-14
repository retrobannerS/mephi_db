from database import Base
from sqlalchemy.orm import Mapped
from custom_types import intpk, str_100


class Menus(Base):
    __tablename__ = "menus"

    id: Mapped[intpk]
    title: Mapped[str_100]
    cost: Mapped[float]
    count_dishes: Mapped[int]
    colorfulness: Mapped[float]
