from database import Base
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from custom_types import intpk, str_100
import enum

class Status(enum.Enum):
    NEW = "new"
    IN_DELIVERY = "in_delivery"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    RETURNED = "returned"

class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    menu_id: Mapped[int | None] = mapped_column(
        ForeignKey("menus.id", ondelete="SET NULL")
    )
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("now()"))
    status: Mapped[Status] = mapped_column(server_default=text("'new'"))
    courier_id: Mapped[int | None] = mapped_column(
        ForeignKey("couriers.id", ondelete="SET NULL")
    )
    payment_info_id: Mapped[int | None] = mapped_column(
        ForeignKey("payment_infos.id", ondelete="SET NULL")
    )
