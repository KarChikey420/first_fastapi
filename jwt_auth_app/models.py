from sqlalchemy import Integer,Column,String
from .database import Base

class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(20),unique=True,nullable=False,index=True)
    email=Column(String(20), unique=True, nullable=False, index=True)
    hashed_password=Column(String)
    