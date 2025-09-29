import uvicorn
from fastapi import FastAPI
from sqlalchemy import Integer,String, create_engine,column
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

SqolAlchemy_URL = "sqlite:///./crud.db"
engine=create_engine(SqolAlchemy_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()




    