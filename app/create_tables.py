from database import Base, engine
import models


def create_tables():
    engine.echo = False
    Base.metadata.drop_all(engine)
    engine.echo = True
    Base.metadata.create_all(engine)
