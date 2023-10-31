from peewee import Model
from peewee import CharField, DateTimeField, IntegerField, DecimalField, ForeignKeyField
from db.database import database

from datetime import datetime

class BaseModel(Model):
    class Meta:
        database=database
        createdAt = DateTimeField(default=datetime.now)
        updatedAt = DateTimeField(default=datetime.now)
        
class Collection(BaseModel):
    name = CharField(max_length=100, unique=True)

class Units(BaseModel):
    name = CharField(max_length=10, unique=True)
      
    
class Product(BaseModel):
    name = CharField(max_length=100, unique=True)
    code = CharField(max_length=10, unique=True)
    amount = IntegerField(default=0)
    cost = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    unit = ForeignKeyField(Units, backref='products')
