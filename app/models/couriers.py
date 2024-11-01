from database import Base
from sqlalchemy.orm import Mapped
import datetime
from custom_types import intpk, str_100

class Couriers(Base):
    __tablename__ = "couriers"

    id: Mapped[intpk]
    first_name: Mapped[str_100]
    middle_name: Mapped[str_100 | None]
    last_name: Mapped[str_100]
    birth_date: Mapped[datetime.date]