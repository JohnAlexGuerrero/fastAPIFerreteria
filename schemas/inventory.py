from pydantic import BaseModel

class EntryItem(BaseModel):
    product_id: int
    amount: int
    price: float
    createdAt: str
    