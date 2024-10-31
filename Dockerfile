FROM python:alpine

WORKDIR /app

# Установка зависимостей для psycopg2
RUN apk add --no-cache gcc musl-dev postgresql-dev

# Установка Python-зависимостей
RUN pip install SQLAlchemy psycopg2

COPY . .

CMD [ "python", "./main.py" ]