from fastapi import FastAPI, Depends
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session


DATABASE_URL = "postgresql://postgres:root@localhost:5432/mydb"
print("database connected successfully!")
engine=create_engine(DATABASE_URL)
sessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
base=declarative_base()

class Student(base):
    __tablename__="school"
    id=Column(Integer,primary_key=True,index=True)
    class_name=Column(String(20))
    name=Column(String(20))
    fees=Column(Integer)
    
app=FastAPI()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/school/")
def get_students(db:Session=Depends(get_db)):
    return db.query(Student).all()

@app.post("/school/")
def create_student(id:int,class_name:str,name:str,fees:int,db:Session=Depends(get_db)):
    new_student=Student(id=id,class_name=class_name,name=name,fees=fees)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
