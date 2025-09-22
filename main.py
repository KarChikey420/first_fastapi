from fastapi import FastAPI
from modules import product

app=FastAPI()

@app.get("/")
def greet():
    return {'message':'you are my honey bunny'}

product_list = [
    product(id=1, name="abc", classes="class1"),
    product(id=2, name="def", classes="class2"),
    product(id=3, name="ghi", classes="class3")
]

@app.get("/products")
def get_all_product():
    return product_list

@app.get("/product/{id}")
def get_one_product(id:int):
    for product in product_list:
       if product.id== id:
           return product
       
    return {"meassage":"not in list"}

@app.post("/product")
def add_product(product:product):
    product_list.append(product)
    return product