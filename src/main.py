from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, main_schemas
from .database import SessionLocal
from celery_service.tasks import add, mul


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    add.apply_async((3,10), queue='myadd')
    mul.apply_async((3,10), queue='mymul')
    return {"Hello": "World"}

@app.post("/users/", response_model=main_schemas.User)
def create_user(user: main_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
