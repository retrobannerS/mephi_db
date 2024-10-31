from database import engine
from sqlalchemy import text

with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res.all()=}")

