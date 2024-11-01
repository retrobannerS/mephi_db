import os
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker

engine = create_engine(os.getenv("DSN"), echo=False)

session = sessionmaker(engine)
