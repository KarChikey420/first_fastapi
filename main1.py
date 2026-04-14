from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app= FastAPI()

class Item(BaseModel):
    username: str
    password: str
    
login_details=[{
    "username": "admin",
    "password": "admin123"
}]

@app.post("/login")
def login(item:Item):
    for details in login_details:
        if item.username == details['username'] and item.password == details['password']:
            return {"message":"Login successful"}
        return {"message":"Invalid username or password"}
    
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
    