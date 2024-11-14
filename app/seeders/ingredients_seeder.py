from database import session
from models import Ingredients
import csv
import os


def seed_ingredients():
    file_path = os.path.join(os.path.dirname(__file__), "csv", "ingredients.csv")
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        ingredients = []

        for row in reader:
            ingredient = Ingredients(
                title=row["title"], type=row["type"], cost=float(row["cost"])
            )
            ingredients.append(ingredient)

    session.bulk_save_objects(ingredients)
    session.commit()
