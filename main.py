from fastapi import FastAPI

app = FastAPI()

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
async def create_product(post):
    return post

@app.put('/product/:id/update')
async def update_product(id):
    return {}

@app.post('/inventory/p/:id/stock')
async def add_stock_product(id):
    return {}

