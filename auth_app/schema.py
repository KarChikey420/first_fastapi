from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    id:int
    user_name:str
    password:str
    email:EmailStr
    
class user_login(BaseModel):
    user_name:str
    password:str
    
class user_response(BaseModel):
    id:int
    user_name:str
    email:EmailStr
    class Config:
        from_attributes=True