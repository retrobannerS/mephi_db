from database import session
from models import Ingredients, Suppliers, Ingredients_Suppliers
import random

def seed_ingredients_suppliers():
    ingredients = session.query(Ingredients).all()
    suppliers = session.query(Suppliers).all()

    ingredients_suppliers = []
    for ingredient in ingredients:
        random_suppliers = random.sample(suppliers, k=random.randint(1, 5))

        for supplier in random_suppliers:
            ingredients_suppliers.append(
                Ingredients_Suppliers(ingredient_id=ingredient.id, supplier_id=supplier.id)
            )

    session.bulk_save_objects(ingredients_suppliers)
    session.commit()