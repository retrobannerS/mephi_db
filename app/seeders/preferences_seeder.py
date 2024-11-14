from models import Preferences
from database import session

def seed_preferences():
    preferences = [
        {"title": "Без творога", "preference_category_id": 1},
        {"title": "Без орехов", "preference_category_id": 1},
        {"title": "Без меда", "preference_category_id": 1},
        {"title": "Без морепродуктов", "preference_category_id": 1},
        {"title": "Без горчицы", "preference_category_id": 1},
        {"title": "Без шоколада", "preference_category_id": 1},
        
        {"title": "Без десертов", "preference_category_id": 2},
        {"title": "Без выпечки", "preference_category_id": 2},
        {"title": "Без сэндвичей и круассанов", "preference_category_id": 2},
        {"title": "Без белого сахара", "preference_category_id": 2},
        
        {"title": "Без свинины и ветчины", "preference_category_id": 3},
        {"title": "Без красного мяса", "preference_category_id": 3},
        {"title": "Без рыбы", "preference_category_id": 3},
        {"title": "Без мяса и птицы", "preference_category_id": 3},
        
        {"title": "Без сельдерея", "preference_category_id": 4},
        {"title": "Без грибов", "preference_category_id": 4},
        {"title": "Без стручковой фасоли", "preference_category_id": 4},
        {"title": "Без брокколи", "preference_category_id": 4},
        {"title": "Без кабачков", "preference_category_id": 4},
        {"title": "Без лука", "preference_category_id": 4},
        {"title": "Без чеснока", "preference_category_id": 4},
        
        {"title": "Без нута", "preference_category_id": 5},
        {"title": "Без булгура", "preference_category_id": 5},
        {"title": "Без кускуса", "preference_category_id": 5},
        {"title": "Без гречки", "preference_category_id": 5},
        {"title": "Без молочных каш", "preference_category_id": 5}
    ]

    session.bulk_insert_mappings(Preferences, preferences)
    session.commit()
