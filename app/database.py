import os
from sqlalchemy import create_engine

engine = create_engine(os.getenv("DSN"), echo=False)