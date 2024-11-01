from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import enum
import datetime
from custom_types import intpk


class Gender(enum.Enum):
    male = "male"
    female = "female"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    first_name: Mapped[str]
    middle_name: Mapped[str | None]
    last_name: Mapped[str]
    sex: Mapped[Gender]
    invited_by: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL")
    )
