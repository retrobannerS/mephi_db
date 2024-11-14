from models import Suppliers
from database import session
from faker import Faker
import random

fake = Faker("ru_RU")


def seed_suppliers(n=10):
    suppliers = [
        Suppliers(title=fake.company(), productivity=random.randint(1, 200))
        for _ in range(n)
    ]

    session.bulk_save_objects(suppliers)
    session.commit()
