from fastapi import FastAPI

from validations.inventory import Item_inventory
from validations.product import Item

from db.database import database
from models.product import Product, Units
from models.inventory import Inventory

app = FastAPI()

database.create_tables([
    Units, Product,
    Inventory    
])

@app.get('/')
async def home():
    return {"message":"Hello World"}

@app.get('/inventory')
async def inventory():
    return {}

@app.get('/inventory/p/:id')
async def get_product(id):
    return {}

@app.post('/inventory/new')
def name(item: Item_inventory):
    product, amount, price = [field for field in item.dict().values()]
    item_in_inventory = Inventory.create(product_id=product, amount=amount, price=price)
    return {"message":"200 ok", "item":item_in_inventory}

@app.post('/inventory/p/:id/stock')
async def add_stock_product(id):
    return {}

@app.post('/product/new')
async def create_product(item: Item):
    name, code, amount, cost, unit_id  = [field for field in item.dict().values()]
    product = Product.create(name=name, code=code, unit_id=unit_id)
    return {"message":"product was created", "item": product}

@app.get('/products/all')
async def all_products(skip: int = 0, limit: int = 10):
    products = Product.select()
    return {"items": products[skip: skip + limit]}

@app.put('/product/:id/update')
async def update_product(id):
    return {}



