from peewee import Model
from peewee import CharField, DecimalField, DateTimeField, BooleanField, IntegerField, ForeignKeyField

from db.database import database
from datetime import datetime

from models.product import Product

class BaseModel(Model):
    class Meta:
        database=database
        
class Shopping(BaseModel):
    num_bill = CharField(max_length=20, unique=True)
    name = CharField(max_length=50, unique=False, null=True)
    total = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    items_total = IntegerField(default=0)
    is_credit = BooleanField(default=False)
    createdAt = DateTimeField(default=datetime.now())
    expirationAt = DateTimeField(default=datetime.now())

class ShoppingDetail(BaseModel):
    shopping = ForeignKeyField(Shopping, backref='orders')
    product = ForeignKeyField(Product, backref='orders')
    amount = IntegerField(default=0)
    price = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    createdAt = DateTimeField(default=datetime.now())
    