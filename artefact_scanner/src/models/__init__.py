from peewee import PostgresqlDatabase
import os

uri = os.environ.get("SQLALCHEMY_DATABASE_URI", "postgresql://administrator:verySecretPassword@localhost:5432/db")
db = PostgresqlDatabase(uri)
