from sqlalchemy import Column, Integer, String, Date, ARRAY

from database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date = Column(String, index=True)
    time = Column(String)
    # repeat_in_days = Column(ARRAY(Integer))
