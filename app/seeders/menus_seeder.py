from database import session
import models


def seed_menus():
    menus = [
        models.Menus(title="Похудение", cost=700, count_dishes=3, colorfulness=1000),
        models.Menus(title="Баланс", cost=850, count_dishes=4, colorfulness=1500),
        models.Menus(title="Набор", cost=1000, count_dishes=5, colorfulness=2000),
    ]

    session.bulk_save_objects(menus)
    session.commit()
