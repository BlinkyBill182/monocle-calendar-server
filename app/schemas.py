from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


class EventBase(BaseModel):
    title: str
    date: str
    time: str
    # repeat_in_days: Union[List[int], None]


class EventCreate(EventBase):
    pass


class Event(EventBase):
    class Config:
        orm_mode = True
