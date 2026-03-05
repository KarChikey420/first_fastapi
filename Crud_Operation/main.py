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

@app.get("/")
def get_data():
    return product_list

@app.post("/add")
def add_prduct(product:product):
    product_list.append(product)
    return {"message":"product added successfully"}

@app.put("/update/{id}")
def update_product(id:int, product:product):
    for p in product_list:
        if p.id==p:
            p.name=product.name
            p.classes=product.classes
    return {"message":"product update successfully"}

@app.delete("/delete/{id}")
def delete_product(id:int):
    for p in product_list:
        if p.id==id:
            product_list.remove(p)
    return {"message":"product deleted successfully"}