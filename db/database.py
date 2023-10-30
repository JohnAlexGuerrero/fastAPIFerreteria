from peewee import MySQLDatabase
from db.variables import NAME_DATABASES, USER, PASSWORD

database = MySQLDatabase(NAME_DATABASES, user=USER, password=PASSWORD)

database.connect()