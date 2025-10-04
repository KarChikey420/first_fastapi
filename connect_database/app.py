from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

DATABASE_URL = "postgresql://postgres:root@localhost:5432/mydb"
print("database connected successfully!")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# ORM Model
class StudentORM(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String(20))
    name = Column(String(20))
    fees = Column(Integer)

Base.metadata.create_all(bind=engine)

# Pydantic Schema
class StudentSchema(BaseModel):
    id: int
    class_name: str
    name: str
    fees: int

    class Config:
        orm_mode = True   # Important: allows returning ORM objects directly

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/school/")
def get_students(db: Session = Depends(get_db)):
    return db.query(StudentORM).all()  # ✅ use ORM class

@app.post("/school/")
def create_student(student: StudentSchema, db: Session = Depends(get_db)):
    new_student = StudentORM(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.put("/school/{id}")
def update_student(id: int, student: StudentSchema, db: Session = Depends(get_db)):
    student_obj = db.query(StudentORM).filter(StudentORM.id == id).first()
    student_obj.class_name = student.class_name
    student_obj.name = student.name
    student_obj.fees = student.fees
    db.commit()
    db.refresh(student_obj)
    return student_obj

@app.delete("/school/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    student_obj = db.query(StudentORM).filter(StudentORM.id == id).first()
    db.delete(student_obj)
    db.commit()
    return {"message": "student is successfully deleted"}
