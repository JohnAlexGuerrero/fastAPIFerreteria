from db.database import database
from peewee import Model
from datetime import datetime
from peewee import CharField, IntegerField, DecimalField, ForeignKeyField, DateTimeField

from models.product import Product

class BaseModel(Model):
    class Meta:
        database=database

class Inventory(BaseModel):
    product = ForeignKeyField(Product, backref='inventories')
    amount = IntegerField(default=0)
    price = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    createdAt = DateTimeField(default=datetime.now)