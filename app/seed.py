from seeders import *


def seed_all():
    seed_payment_methods()
    seed_users(10)
    