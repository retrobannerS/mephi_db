from seeders import *


def seed_all():
    seed_payment_methods()
    seed_users(15000)
    seed_payment_infos()

    seed_couriers(1000)
    seed_menus()
    seed_orders(50000, 100)

    seed_preference_categories()
    seed_preferences()
    seed_preferences_users()

    seed_suppliers(500)
    seed_ingredients()
    seed_ingredients_suppliers()
    seed_dishes()
    seed_dishes_ingredients()
    seed_ingredients_preferences()
    seed_dishes_menus()
