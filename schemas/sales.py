from pydantic import BaseModel
from typing import List
from models.sales import OrderDetail

class OrderDetailSchema(BaseModel):
    product: int
    amount: float
    price: float
    total: float

class Order(BaseModel):
    items: List[OrderDetailSchema]
    
class SalesData(BaseModel):
    client: int
    num_bill: str
    items_total: int
    is_delivery: bool
    is_credit: bool
    subtotal: float
    tax: float
    total: float
    createdAt: str
    expirationAt: str
    comments: str | None=None
    order: List | None=[]
    