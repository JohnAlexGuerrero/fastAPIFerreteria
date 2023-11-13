from pydantic import BaseModel
# from typing import List
from schemas.inventory import EntryItem

class ShoppingSchema(BaseModel):
    num_bill: str
    name: str
    createdAt: str
    expirationAt: str
    is_credit: bool
    total: float
    items_total: int
    # order: list[dict]