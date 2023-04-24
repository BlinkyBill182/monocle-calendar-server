from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/events/", response_model=schemas.Event)
def create_user(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = crud.get_event_by_date_and_time(db, date=event.date, time=event.time)
    if db_event:
        raise HTTPException(status_code=400, detail="Already has event")
    return crud.create_event(db=db, event=event)


@app.get("/events/", response_model=List[schemas.Event])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_events(db, skip=skip, limit=limit)
    return items
