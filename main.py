from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine
import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    user = models.User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    return {"message": "User created"}

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()