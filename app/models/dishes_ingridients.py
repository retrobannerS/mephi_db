from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from custom_types import intpk


class DishesIngridients(Base):
    __tablename__ = "dishes_ingridients"

    id: Mapped[intpk]
    dish_id: Mapped[int] = mapped_column(ForeignKey("dishes.id", ondelete="CASCADE"))
    ingridient_id: Mapped[int] = mapped_column(ForeignKey("ingridients.id", ondelete="CASCADE"))
