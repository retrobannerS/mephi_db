from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from custom_types import intpk

class Preferences_Users(Base):
    __tablename__ = "preferences_users"
    id: Mapped[intpk]
    preference_id: Mapped[int] = mapped_column(ForeignKey("preferences.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))