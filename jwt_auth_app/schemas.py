from pydantic import BaseModel,EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    username:str
    id:int
    email:str
    
    class Config:
        from_attributes=True

class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    username:Optional[str]=None
    