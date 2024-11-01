from sqlalchemy import ForeignKey
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from custom_types import intpk


class Payment_infos(Base):
    __tablename__ = "payment_infos"
    id: Mapped[intpk]
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    payment_method_id: Mapped[int | None] = mapped_column(
        ForeignKey("payment_methods.id", ondelete="CASCADE")
    )
    requisites: Mapped[str] = mapped_column(nullable=True)
