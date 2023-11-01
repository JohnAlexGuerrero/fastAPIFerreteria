from fastapi import FastAPI, UploadFile, File
import pandas as pd
from typing import Annotated
from secrets import token_hex
from openpyxl import Workbook, load_workbook

from validations.product import Item

from db.database import database
from models.product import Product, Units
from models.inventory import Inventory

app = FastAPI(title='Soluciones Ferreteras Api')

database.create_tables([
    Units, Product,
    Inventory   
])

@app.get('/')
async def home():
    return {"message":"Hello World"}

@app.get('/inventory')
async def inventory():
    return {"products":[
        { 
         "id":1,"codebar":"456458", "name":"teja trapezoidal 3,0m","brand":"no aplica","category":"tejas", "stock":23, "unit":"und",
         "createdAt":"2023-12-02","updatedAt":"2023-02-23"
        }
    ]}

@app.get('/inventory/p/:id')
async def get_product(id):
    return {}

@app.post('/product/new')
async def create_product(item: Item):
    name, code, amount, cost, unit_id = [f for f in item.dict().values()]
    product = Product.create(name=name, code=code, unit_id=unit_id)
    return {"item_created": product}

@app.put('/product/:id/update')
async def update_product(id):
    return {}

@app.post('/inventory/p/:id/stock')
async def add_stock_product(id):
    return {}

'''
crear un endpoint en FastAPI que permita importar datos desde un archivo Excel para la creación de productos
'''
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/import/products/")
async def create_upload_file(file: UploadFile = File(...)):
    if file.filename.endswith('.xlsx'):
      file_name = f'{file.filename}{token_hex(10)}'
      file_path = f"{file_name}.xlsx"
      
      with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
        
    items_from_excel(file_path)
    return {"filename": file_name, 'path': file_path}

def items_from_excel(file):
    name_units = ['und', 'mtr','kl','mtr2']
    df = pd.read_excel(file)
    df['unit'] = df.unit.apply(lambda x: name_units.index(x) + 1)
    
    for x in range(len(df)):
        item = Product.create(name=df.name[x], code=df.code[x],unit_id=df.unit[x])
    