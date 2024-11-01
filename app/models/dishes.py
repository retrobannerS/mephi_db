from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from custom_types import intpk, str_100


class Dishes(Base):
    __tablename__ = "dishes"

    id: Mapped[intpk]
    title: Mapped[str_100]
    type: Mapped[str_100]
    weight: Mapped[float]
    colorfulness: Mapped[float]
