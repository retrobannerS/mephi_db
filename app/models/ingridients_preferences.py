from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from custom_types import intpk

class IngridientsPreferences(Base):
    __tablename__ = "ingridients_preferences"
    id: Mapped[intpk]
    ingridient_id: Mapped[int] = mapped_column(ForeignKey("ingridients.id", ondelete="CASCADE"))
    preference_id: Mapped[int] = mapped_column(ForeignKey("preferences.id", ondelete="CASCADE"))