from database import session
from models import Ingredients_Preferences
import csv
import os


def seed_ingredients_preferences():
    file_path = os.path.join(os.path.dirname(__file__), "csv", "ingredients_preferences.csv")
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        values = []

        for row in reader:
            value = Ingredients_Preferences(
                ingredient_id=row["ingredient_id"],
                preference_id=row["preference_id"]
            )
            values.append(value)

    session.bulk_save_objects(values)
    session.commit()