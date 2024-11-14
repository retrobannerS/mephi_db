from database import session
import models
import random
import datetime
from faker import Faker

fake = Faker("ru_RU")

def generate_order_created_time(duration):
    """Генерация даты рождения в диапазоне от min_age до max_age лет назад."""
    now = datetime.datetime.now()
    start_time = now - datetime.timedelta(days=duration)
    return fake.date_time_between(start_date=start_time, end_date=now)

def seed_orders(n=100):
    users = session.query(models.Users).all()
    menus = session.query(models.Menus).all()
    couriers = session.query(models.Couriers).all()
    payment_infos = (
        session.query(models.Payment_infos)
        .filter(models.Payment_infos.user_id == models.Users.id)
        .all()
    )

    orders = []
    for _ in range(n):
        user = random.choice(users)
        menu = random.choice(menus)
        courier = random.choice(couriers)
        payment_info = random.choice(payment_infos)

        order = models.Orders(
            user_id=user.id,
            menu_id=menu.id,
            created_at=generate_order_created_time(30),
            status=random.choice(list(models.Status)),
            courier_id=courier.id if courier else None,
            payment_info_id=payment_info.id if payment_info else None,
        )

        user.bonuses += menu.cost * 0.05

        orders.append(order)

    session.bulk_save_objects(orders)
    session.commit()
    session.flush()

    session.commit()
