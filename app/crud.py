from datetime import datetime

from sqlalchemy.orm import Session

import models
import schemas


def create_event(db: Session, event: schemas.EventCreate):
    # db_event = models.Event(date=event.date, time=event.time, title=event.title, repeat_in_days=event.repeat_in_days)
    db_event = models.Event(date=event.date, time=event.time, title=event.title)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


def get_event_by_date_and_time(db: Session, title: str):
    return db.query(models.Event).filter(models.Event.title == title).first()
