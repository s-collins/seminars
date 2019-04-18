from sqlalchemy import Column, Integer, String, ForeignKey, Table
from .Base import DeclarativeBase

# association table between Event and Tags
event_has_tag = Table(
	'Event_has_Tag',
	DeclarativeBase.metadata,
	Column('event_id', Integer, ForeignKey('Event.event_id')),
	Column('tag_text', String(100), ForeignKey('Tag.tag_text'))
)