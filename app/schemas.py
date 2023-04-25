from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


class EventBase(BaseModel):
    id: int
    title: str
    date: str
    time: str
    # repeat_in_days: Union[List[int], None]


class EventCreate(BaseModel):
    title: str
    date: str
    time: str


class Event(EventBase):
    class Config:
        orm_mode = True
