from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from custom_types import intpk


class IngridientsSuppliers(Base):
    __tablename__ = "ingridients_suppliers"

    id: Mapped[intpk]
    ingridient_id: Mapped[int] = mapped_column(ForeignKey("ingridients.id", ondelete="CASCADE"))
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id", ondelete="CASCADE"))
