from sqlalchemy import Column, Integer, String, Date

from database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date = Column(Date, index=True)
    time = Column(Date)
    repeat_in_days = Column(String, nullable=True)
