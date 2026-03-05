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

@app