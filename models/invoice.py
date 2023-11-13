from peewee import Model
from peewee import CharField, DecimalField, DateTimeField

from db.database import database
from datetime import datetime

class BaseModel(Model):
    class Meta:
        database=database
        
class Invoice(BaseModel):
    pass    