from database import Base
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
import enum
import datetime
from custom_types import intpk, phone_number, str_100


class Gender(enum.Enum):
    male = "male"
    female = "female"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    first_name: Mapped[str_100]
    middle_name: Mapped[str_100 | None]
    last_name: Mapped[str_100]
    sex: Mapped[Gender | None]
    birth_date: Mapped[datetime.date]
    phone_number: Mapped[phone_number]
    invited_by_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL")
    )
    bonuses: Mapped[int] = mapped_column(server_default=text("0"))
    address: Mapped[str_100 | None]
