import os
from sqlalchemy import create_engine, text

engine = create_engine(os.getenv("DSN"), echo=False)

with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res.all()=}")

