from pydantic import BaseModel

class Item(BaseModel):
    name: str
    code: str
    amount: int | None = None
    cost: float | None = None
    unit_id: int

class PriceProduct(BaseModel):
    product_id: int
    price: float
    createdAt: str