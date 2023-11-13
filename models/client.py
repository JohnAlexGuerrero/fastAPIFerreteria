from peewee import Model
from peewee import CharField, DateTimeField
from db.database import database

from datetime import datetime

class BaseMode(Model):
    class Meta:
        database=database

class Client(BaseMode):
    full_name = CharField(max_length=50, null=False)
    num_document = CharField(max_length=20, null=True)
    address = CharField(max_length=50, null=True)
    email = CharField(max_length=50, null=True)
    phone = CharField(max_length=20, null=True)
    createdAt = DateTimeField(default=datetime.now())
    updatedAt = DateTimeField(default=datetime.now())