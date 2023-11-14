from fastapi import FastAPI, UploadFile, File
import pandas as pd
from typing import Annotated
from typing import List

from schemas.product import Item, PriceProduct
from schemas.inventory import EntryItem
from schemas.client import ClientSchema
from schemas.sales import SalesData, OrderDetail
from schemas.shopping import ShoppingSchema

from db.database import database
from models.product import Product, Units
from models.inventory import Inventory
from models.client import Client
from models.sales import Invoice, OrderDetail
from models.shopping import Shopping, ShoppingDetail

app = FastAPI(title='Soluciones Ferreteras Api')

database.create_tables([
    Units, Product,
    Inventory,
    Client,
    Invoice, OrderDetail,
    Shopping, ShoppingDetail
])

'''# function for get one item of product table'''
def get_product_db(id:int)->Product:
    product = Product.get(Product.id == id)
    return product

'''# function for get registers of inventory table with id'''
def all_inventories_db(id)->[]:
    items = Inventory.select().where(Inventory.product_id == id).order_by(Inventory.createdAt)
    return [item for item in items]

@app.get('/products/', status_code=200)
async def get_products():
    products = Product.select()
    items = [item for item in products]
    
    return {"items": items}

@app.patch('/products/update/price/', status_code=202)
async def update_price(price_product: PriceProduct):
    p = dict(price_product)
    product = Product.update(price=p['price'], updatedAt=p['createdAt']).where(Product.id == p['product_id'])
    if product != None:
        product.execute()
    return {"message":"precio actualizado."}

@app.post('/product/new')
async def create_product(item: Item):
    name, code, amount, cost, unit_id = [f for f in item.dict().values()]
    product = Product.create(name=name, code=code, unit_id=unit_id)
    return {"item_created": product}

@app.put('/product/:id/{item_id}')
async def show_product(item_id:int):
    product = get_product_db(item_id)
    items = all_inventories_db(item_id)
    
    data = {
            "id": product.id,
            "name": product.name,
            "amount": product.amount,
            "unit": product.unit.name,
            "cost": product.cost,
            "price": product.price,
        }
    
    return {"item":data, "inventory":items}

@app.post('/inventory/new', status_code=201)
async def add_item_inventory(item: EntryItem):
    item = Inventory.create(**dict(item))

def add_item_shopping(id_shopping: int, item: EntryItem):
    data = dict(item)
    data['shopping_id'] = id_shopping
    data['total']: data.price * data.amount
    
    item = ShoppingDetail.create(**data)
    print(data)

# '''
# crear un endpoint en FastAPI que permita importar datos desde un archivo Excel para la creación de productos
# '''
# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


# @app.post("/import/products/")
# async def create_upload_file(file: UploadFile = File(...)):
#     if file.filename.endswith('.xlsx'):
#       file_name = f'{file.filename}{token_hex(10)}'
#       file_path = f"{file_name}.xlsx"
      
#       with open(file_path, "wb") as f:
#         content = await file.read()
#         f.write(content)
        
#     items_from_excel(file_path)
#     return {"filename": file_name, 'path': file_path}

# def items_from_excel(file):
#     name_units = ['und', 'mtr','kl','mtr2']
#     df = pd.read_excel(file)
#     df['unit'] = df.unit.apply(lambda x: name_units.index(x) + 1)
    
#     for x in range(len(df)):
#         item = Product.create(name=df.name[x], code=df.code[x],unit_id=df.unit[x])

'''
sales
'''
@app.post('/clients/new', status_code=201)
async def create_client(client:ClientSchema):
    client = Client.create(**dict(client))
    return {"message":"cliente fue creado con exito."}

@app.post('/sales/', status_code=201)
async def save_sale(data:SalesData):
    # print(dict(data))
    print(data.orders)
    
    return {}

@app.post('/shoppings/', status_code=201)
async def add_shopping(shopping: ShoppingSchema, order: List[EntryItem]):
    bill_dict = dict(shopping)
    new_shopping = Shopping.create(**bill_dict)
    
    if new_shopping != None:
        for item in order:
            add_item_shopping(new_shopping.id, item)
            print(new_shopping.id)
    else:
        return {"message": 'no fue posible.'}
    
    return {"message":"fue agregado con exito."}