from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = crud.get_event_by_date_and_time(db, title=event.title)
    if db_event:
        raise HTTPException(status_code=400, detail="Already has event")
    return crud.create_event(db=db, event=event)


@app.get("/events/", response_model=List[schemas.Event])
def get_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_events(db, skip=skip, limit=limit)
    return items
