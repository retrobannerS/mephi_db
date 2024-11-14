from database import session
import models
import random
import datetime
from faker import Faker

fake = Faker("ru_RU")


def generate_order_created_time(duration):
    now = datetime.datetime.now()
    start_time = now - datetime.timedelta(days=duration)
    return fake.date_time_between(start_date=start_time, end_date=now)


def generate_order_status(created_time):
    now = datetime.datetime.now()
    if now - created_time <= datetime.timedelta(days=1):
        status_weights = {
            models.Status.new: 0.5,
            models.Status.in_delivery: 0.5,
        }
        status = random.choices(
            list(status_weights.keys()), list(status_weights.values()), k=1
        )[0]
    elif datetime.timedelta(days=1) < now - created_time <= datetime.timedelta(days=3):
        status_weights = {models.Status.in_delivery: 0.1, models.Status.delivered: 0.9}
        status = random.choices(
            list(status_weights.keys()), list(status_weights.values()), k=1
        )[0]
    else:
        status = models.Status.delivered

    if status == models.Status.delivered and random.random() < 0.05:
        status = models.Status.returned

    if random.random() < 0.05:
        status = models.Status.cancelled

    return status


def seed_orders(n=100, duration=30):
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
        created_at = generate_order_created_time(duration)

        order = models.Orders(
            user_id=user.id,
            menu_id=menu.id,
            created_at=created_at,
            status=generate_order_status(created_at),
            courier_id=courier.id,
            payment_info_id=payment_info.id,
        )

        user.bonuses += menu.cost * 0.05
        user.address = fake.street_address()

        orders.append(order)

    session.bulk_save_objects(orders)
    session.commit()
    session.flush()

    session.commit()
