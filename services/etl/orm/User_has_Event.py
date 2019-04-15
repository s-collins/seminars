from sqlalchemy import Column, Integer, ForeignKey, String, Table
from .Base import DeclarativeBase


# association table between User and Event
user_has_event = Table(
	'User_has_Event',
	DeclarativeBase.metadata,
	Column('user_email', String(200), ForeignKey('User.email')),
	Column('event_id', Integer, ForeignKey('Event.event_id'))
)