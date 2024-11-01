from database import Base
from sqlalchemy.orm import Mapped
from custom_types import intpk, str_100


class Suppliers(Base):
    __tablename__ = "suppliers"

    id: Mapped[intpk]
    title: Mapped[str_100]
    productivity: Mapped[float]
