from database import session
from faker import Faker
import models
import random

fake = Faker("ru_RU")

def seed_payment_infos():
    users = session.query(models.Users).all()
    payment_methods = session.query(models.Payment_Methods).all()
    
    payment_infos = []
    for user in users:
        payment_method = random.choice(payment_methods)
        
        payment_info = models.Payment_infos(
            user_id=user.id,
            payment_method_id=payment_method.id if random.random() > 0.3 else None,
            requisites=fake.credit_card_number() if payment_method.require_requisites else None
        )
        payment_infos.append(payment_info)
    
    session.bulk_save_objects(payment_infos)
    session.commit()
