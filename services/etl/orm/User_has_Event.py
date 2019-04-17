from sqlalchemy import Column, Integer, ForeignKey, String, Table
from .Base import DeclarativeBase


# association table between User and Event
user_has_event = Table(
	'User_has_Event',
	DeclarativeBase.metadata,
	Column('username', String(200), ForeignKey('User.username')),
	Column('event_id', Integer, ForeignKey('Event.event_id'))
)