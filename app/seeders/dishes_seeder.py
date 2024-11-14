from database import session
from models import Dishes
import csv
import os


def seed_dishes():
    file_path = os.path.join(os.path.dirname(__file__), "csv", "dishes.csv")
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        dishes = []

        for row in reader:
            dish = Dishes(
                title=row["title"], type=row["type"], weight=float(row["weight"]), colorfulness=float(row["colorfulness"]),
            )
            dishes.append(dish)

    session.bulk_save_objects(dishes)
    session.commit()