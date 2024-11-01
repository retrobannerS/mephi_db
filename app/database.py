import os
from sqlalchemy import create_engine, String
from sqlalchemy.orm import session, sessionmaker, DeclarativeBase
from custom_types import phone_number

engine = create_engine(url=os.getenv("DSN"), echo=True)

session = sessionmaker(engine)

class Base(DeclarativeBase):
    type_annotation_map = {phone_number: String(10)}
