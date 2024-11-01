from sqlalchemy.orm import Mapped
from custom_types import str_100, intpk
from database import Base

class Payment_Methods(Base):
    __tablename__ = "payment_methods"
    id: Mapped[intpk]
    title: Mapped[str_100]
    