from database import session
from models import Dishes_Menus, Dishes, Menus
import datetime, random


def seed_dishes_menus():
    # Задаем диапазон дат на месяц вперед
    today = datetime.date.today()
    date_range = [today + datetime.timedelta(days=i) for i in range(30)]

    # Получаем все меню
    menus = session.query(Menus).all()
    dishes = session.query(Dishes).all()
    values = []
    for date in date_range:
        for menu in menus:
            selected_dishes = []
            colorfulness_accumulated = 0

            # Пока не выбрано нужное количество блюд для меню
            while len(selected_dishes) < menu.count_dishes:
                # Выбираем случайное блюдо
                dish = random.choice(dishes)

                # Проверяем, укладывается ли блюдо в параметры меню
                if colorfulness_accumulated + dish.colorfulness <= menu.colorfulness:
                    selected_dishes.append(dish)
                    colorfulness_accumulated += dish.colorfulness

            # Добавляем выбранные блюда в dishes_menus
            for dish in selected_dishes:
                value = Dishes_Menus(
                    dish_id=dish.id, menu_id=menu.id, date=date
                )
                values.append(value)

    session.bulk_save_objects(values)
    session.commit()
