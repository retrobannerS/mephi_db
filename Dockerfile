FROM python:alpine

WORKDIR /app

RUN pip install SQLAlchemy psycopg psycopg-binary

COPY ./app .

CMD [ "python", "./main.py" ]