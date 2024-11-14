from database import session
import models


def seed_payment_methods():
    payment_methods = [
        models.Payment_methods(title="Наличные курьеру", require_requisites=False),
        models.Payment_methods(title="Карта курьеру", require_requisites=True),
        models.Payment_methods(title="Карта", require_requisites=True),
        models.Payment_methods(title="Яндекс.Сплит", require_requisites=True),
    ]

    session.bulk_save_objects(payment_methods)
    session.commit()
