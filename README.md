# mephi-db

Лабораторная работа по курсу «Базы данных» в НИЯУ МИФИ.

Тема: GrowFood.

Проект написан на [Python](https://www.python.org) и использует [SQLAlchemy](https://www.sqlalchemy.org) в качестве ORM для [PostgreSQL](https://www.postgresql.org).

<details>
  <summary>ER-диаграмма</summary>
  <p align="center">
    <img src=https://github.com/user-attachments/assets/f9b7139a-fb85-4151-bff0-e80789edbc35 width=50%/>
  </p>
</details>

## Запуск

Проект контейнеризирован. Чтобы запустить проект, убедитесь, что [Docker](https://www.docker.com) установлен на вашем компьютере.

Для запуска необходимо выполнить команду внутри проекта:

```bash
docker-compose up --build
```

## pgadmin

После запуска Вы можете подключиться к `pgadmin` по адресу http://localhost:5050.

Данные для подключения к базе данных (они также редактируются в [.env](./.env))

```plaintext
Host name/address: db
Port: 5432
Username: mephi
Password: mephi
```

| ![ScreenShot 2024-10-31 at 17 44 37](https://github.com/user-attachments/assets/61cf24b7-4c4b-4d62-83a8-317608e5178c) | ![ScreenShot 2024-10-31 at 17 44 59](https://github.com/user-attachments/assets/4df29aa5-a397-40e4-9ea8-2f95e1ca0770) |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |

## Заполнение базы данных

База данных заполняется автоматически при запуске контейнера. Функции заполнения находятся в папке [seed](./app/seeders).

## Запросы

В проекте приведены учебные запросы к базе данных. Примеры готовых запросов находятся в файлах с расширением `.sql` в папке [queries](./queries).

Написание запросов "по шагам" можно посмотреть в [Jupyter Notebook](./queries/notebook.ipynb).

## Отчёт

Отчёт по лабораторной работе написан в формате `markdown` и переведён в `pdf` с помощью [pandoc](https://pandoc.org). Отчёт находится в папке [report](./report). Исходный `markdown` файл вы можете найти [здесь](./report/src/report.md) Для перевода в `pdf` необходимо запустить `python` [скрипт](./report/scripts/build.py). Подробнее о конвертации можно прочитать в [проекте](https://github.com/retrobannerS/pandoc_markdown_build_system).