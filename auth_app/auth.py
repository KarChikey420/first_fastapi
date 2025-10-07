from sqlalchemy.orm import Session
from . import model

def get_user_by_name(db:Session,user_name:str):
    return db.query(model.user).filter(model.User.user_name==user_name).first()

def create_user(db:Session,user_name:str,email:str,password:str):
     db_user=model.User(
         user_name=user_name,
         email=email,
         password=password  
     )
     db.add(db_user)
     db.commit()
     db.refresh(db_user)
     return db_user
 
def verify_password(plain_password:str,stored_password:str):
    return plain_password==stored_password

