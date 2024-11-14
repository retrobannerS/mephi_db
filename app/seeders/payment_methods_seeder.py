from database import session
import models

def seed_payment_methods():
    payment_methods = [
        models.Payment_Methods(title="Наличные курьеру"),
        models.Payment_Methods(title="Карта курьеру"),
        models.Payment_Methods(title="Карта"),
        models.Payment_Methods(title="Яндекс.Сплит")
    ]
    
    session.bulk_save_objects(payment_methods)
    session.commit()
