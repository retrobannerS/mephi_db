FROM python:alpine

WORKDIR /app

RUN pip install SQLAlchemy psycopg psycopg-binary

COPY . .

CMD [ "python", "./main.py" ]