from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    id:int
    username:str
    password:str
    email:EmailStr
    
class user_login(BaseModel):
    username:str
    password:str
    
class user_response(BaseModel):
    id:int
    username:str
    email:EmailStr
    class Config:
        from_attributes=True