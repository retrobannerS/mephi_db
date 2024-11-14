FROM python:alpine

WORKDIR /app

RUN pip install SQLAlchemy psycopg psycopg-binary faker

COPY ./app .

CMD [ "python", "./main.py" ]