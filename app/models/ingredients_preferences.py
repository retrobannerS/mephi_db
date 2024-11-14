from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from custom_types import intpk


class Ingredients_preferences(Base):
    __tablename__ = "ingredients_preferences"
    id: Mapped[intpk]
    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.id", ondelete="CASCADE")
    )
    preference_id: Mapped[int] = mapped_column(
        ForeignKey("preferences.id", ondelete="CASCADE")
    )
