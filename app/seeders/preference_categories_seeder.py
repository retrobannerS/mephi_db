from models import Preference_categories
from database import session

def seed_preference_categories():
    categories = [
        "аллергены",
        "десерты, выпечка, сахар",
        "мясо, рыба",
        "овощи, лук, чеснок",
        "гарниры, каши"
    ]
    session.bulk_save_objects([Preference_categories(title=title) for title in categories])
    session.commit()
