from sqlalchemy.orm import Mapped
from custom_types import str_100, intpk
from database import Base


class Preference_categories(Base):
    __tablename__ = "preference_categories"
    id: Mapped[intpk]
    title: Mapped[str_100]
