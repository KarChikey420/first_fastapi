from sqlalchemy import Column,Integer,String
from .database import Base

class Student(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String(20),unique=True,nullable=False,index=True)
    email=Column(String(20),unique=True,nullable=False,index=True)
    password=Column(String)
    
    
    