from models import Preferences_Users, Users, Preferences
from database import session
import random

def seed_preferences_users():
    users = session.query(Users.id).all()
    preferences = session.query(Preferences.id).all()
    preferences_ids = [pref.id for pref in preferences]

    for user in random.sample(users, int(len(users) * 0.3)):
        selected_prefs = random.sample(preferences_ids, random.randint(1, 5))
        for pref_id in selected_prefs:
            session.add(Preferences_Users(preference_id=pref_id, user_id=user.id))

    session.commit()
