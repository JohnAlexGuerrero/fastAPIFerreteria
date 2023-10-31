from pydantic import BaseModel

class Item_inventory(BaseModel):
    product_id: int
    amount: int
    price: float
    