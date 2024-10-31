# mephi-db

Лабораторная работа по курсу «Базы данных» в НИЯУ МИФИ.

Тема: GrowFood.

Проект написан на [Python](https://www.python.org) и использует [SQLAlchemy](https://www.sqlalchemy.org) в качестве ORM для [PostgreSQL](https://www.postgresql.org).

## Запуск

Проект контейнеризирован. Чтобы запустить проект, убедитесь, что [Docker](https://www.docker.com) установлен на вашем компьютере.

Для запуска необходимо выполнить команду внутри проекта:

```bash
docker-compose up --build
```

## pgadmin

Вы можете подключиться к `pgadmin` по адресу `http://localhost:5050`.

Данные для подключения к базе данных:

```plaintext
Host name/address: db
Port: 5432
Username: mephi
Password: mephi
```

| ![ScreenShot 2024-10-31 at 17 44 37](https://github.com/user-attachments/assets/61cf24b7-4c4b-4d62-83a8-317608e5178c) | ![ScreenShot 2024-10-31 at 17 44 59](https://github.com/user-attachments/assets/4df29aa5-a397-40e4-9ea8-2f95e1ca0770) |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |

