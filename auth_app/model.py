from sqlalchemy import Column,Integer,String
from .database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(20),unique=True,nullable=False,index=True)
    email=Column(String(20),unique=True,nullable=False,index=True)
    password=Column(String)
    
    
    