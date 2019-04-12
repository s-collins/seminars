from sqlalchemy import Column, Integer, ForeignKey, Table
from .Base import DeclarativeBase


# association table between Event and Speaker
event_has_speaker = Table(
    'Event_has_Speaker',
    DeclarativeBase.metadata,
    Column('event_id', Integer, ForeignKey('Event.event_id')),
    Column('speaker_id', Integer, ForeignKey('Speaker.speaker_id'))
)

