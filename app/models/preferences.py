from sqlalchemy import ForeignKey
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from custom_types import intpk, str_100


class Preferences(Base):
    __tablename__ = "preferences"
    id: Mapped[intpk]
    title: Mapped[str_100]
    preference_category_id: Mapped[int] = mapped_column(ForeignKey("preference_categories.id", ondelete="CASCADE"))