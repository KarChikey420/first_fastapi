from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from . import auth, database, model, schema

model.Base.metadata.create_all(bind=database.engine)

app=FastAPI(title="authentication")

@app.post("/register",response_model=schema.user_response,status_code=status.HTTP_201_CREATED)
async def register(user:schema.UserCreate,db:Session=Depends(database.get_db)):
    if auth.get_user_by_name(db,user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="already exist in database"
        )
    new_user=auth.create_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password
    )
    
    return new_user

@app.post("/login")
async def login(
    from_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):
    user=auth.get_user_by_name(db,from_data.username)
    if not user or not auth.verify_password(from_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invailid credential"
        )
