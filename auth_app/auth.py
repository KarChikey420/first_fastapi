from sqlalchemy.orm import Session
from . import model

def get_user_by_name(db:Session,username:str):
    return db.query(model.User).filter(model.User.username==username).first()

def create_user(db:Session,username:str,email:str,password:str):
     db_user=model.User(
         username=username,
         email=email,
         password=password  
     )
     db.add(db_user)
     db.commit()
     db.refresh(db_user)
     return db_user
 
def verify_password(plain_password:str,stored_password:str):
    return plain_password==stored_password

