from peewee import Model
from peewee import IntegerField, CharField, DateTimeField, BooleanField, DecimalField, ForeignKeyField, FloatField, TextField
from datetime import datetime

from db.database import database
from models.product import Product
from models.client import Client

class BaseModel(Model):
    class Meta:
        database=database

class Invoice(BaseModel):
    client = ForeignKeyField(Client, backref='invoices')
    num_bill = CharField(max_length=10, null=False, unique=True)
    items_total = IntegerField(default=0)
    is_delivery = BooleanField()
    is_credit = BooleanField(default=False)
    subtotal = DecimalField(default=0.0)
    tax = FloatField(default=0.0)
    total = DecimalField(default=0.0)
    createdAt = DateTimeField(default=datetime.now())
    expirationdAt = DateTimeField(default=datetime.now())
    comments = TextField(null=True)

class OrderDetail(BaseModel):
    invoice = ForeignKeyField(Invoice, backref='orderdetails')
    product = ForeignKeyField(Product, backref='orderdetails')
    amount = FloatField(default=0.0)
    price = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = DecimalField(max_digits=10, decimal_places=2, default=0.0)