from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app=FastAPI()

class LoginRequest(BaseModel):
    email: str
    password: str

model=[{
    "email":"user@example.com",
    "password":"password123"
}]

@app.post("/signin")
def signin(user: LoginRequest):
    for i in model:
        if i['email']==user.email and i['password']==user.password:
            return {"message":"login successful"}
    return {"message":"invalid email or password"}

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
