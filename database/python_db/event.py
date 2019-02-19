from sqlalchemy import (Table, Column, ForeignKey, Integer, String,
                        Date, Enum, Time)
from sqlalchemy.orm import relationship
from base import Base


event_speaker_association = Table(
    'Event_has_Speaker',
    Column('id_event', Integer, ForeignKey('Event.id_event')),
    Column('id_speaker', Integer, ForeignKey('Speaker.id_speaker'))
)


class Event(Base):
    __tablename__ = 'Event'

    # Relation attributes
    id_event = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    location = Column(String)
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    url = Column(String)
    speakers = relationship('speaker', secondary=event_speaker_association)

    def __init__(self, title, description, location, date, start_time,
                 end_time, url):
        self.title = title
        self.description = description
        self.location = location
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.url = url
