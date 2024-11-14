from database import session
from models import Dishes_Ingredients
import csv
import os


def seed_dishes_ingredients():
    file_path = os.path.join(os.path.dirname(__file__), "dishes_ingredients.csv")
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        values = []

        for row in reader:
            value = Dishes_Ingredients(
                dish_id=row["dish_id"],
                ingredient_id=row["ingredient_id"],
            )
            values.append(value)

    session.bulk_save_objects(values)
    session.commit()
