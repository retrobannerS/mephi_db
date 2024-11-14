from database import session
from faker import Faker
import models
import random
import datetime

fake = Faker("ru_RU")


def generate_phone_number():
    """Форматирует номер телефона в виде 10 цифр без кода страны."""
    return fake.numerify("9#########")


def generate_name_by_gender(gender):
    """Генерация имени, отчества и фамилии в зависимости от пола."""
    if gender == models.Gender.male:
        first_name = fake.first_name_male()
        middle_name = fake.middle_name_male()
        last_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        middle_name = fake.middle_name_female()
        last_name = fake.last_name_female()
    return first_name, middle_name, last_name


def generate_birth_date(min_age=18, max_age=80):
    """Генерация даты рождения в диапазоне от min_age до max_age лет назад."""
    today = datetime.date.today()
    start_date = today.replace(year=today.year - max_age)
    end_date = today.replace(year=today.year - min_age)
    return fake.date_between(start_date=start_date, end_date=end_date)


def seed_users(n=50):
    users = []
    for _ in range(n):
        sex = random.choice([models.Gender.male, models.Gender.female])
        first_name, middle_name, last_name = generate_name_by_gender(sex)

        user = models.Users(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            sex=sex,
            birth_date=generate_birth_date(),
            phone_number=generate_phone_number(),
            address=None,
            bonuses=0,
        )
        users.append(user)

    session.bulk_save_objects(users)
    session.commit()

    all_users = session.query(models.Users).all()
    for user in all_users:
        if random.random() < 0.3:  # 30% пользователей будут иметь "пригласившего"
            user.invited_by_id = random.choice(all_users).id
    session.commit()
