from database import Base, engine
from models.users import Users


def create_tables():
    engine.echo = False
    Base.metadata.drop_all(engine)
    engine.echo = True
    Base.metadata.create_all(engine)
