from db.database import database
from peewee import Model
from peewee import CharField, IntegerField, DecimalField, ForeignKeyField, DateField

from models.product import Product

class BaseModel(Model):
    class Meta:
        database=database

class Inventory(BaseModel):
    product = ForeignKeyField(Product, backref='inventories')
    stock = IntegerField(default=0)
    cost = DecimalField(max_digits=10 , decimal_places=2, default=0.0)
    price = DecimalField(max_digits=10 ,decimal_places=2, default=0.0)
    createdAt = DateField()
    updatedAt = DateField()