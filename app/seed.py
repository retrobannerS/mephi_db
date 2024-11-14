from seeders import *


def seed_all():
    seed_payment_methods()
    seed_users(10)
    seed_payment_infos()

    seed_couriers(5)
    seed_menus()
    seed_orders(50, 30)

    seed_preference_categories()
    seed_preferences()
    seed_preferences_users()

    seed_suppliers(10)
    seed_ingredients()
    seed_ingredients_suppliers()
