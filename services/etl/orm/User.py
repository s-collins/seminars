from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import DeclarativeBase
from .User_has_Event import user_has_event


class User(DeclarativeBase):

	# --------------------------------------------------------------------------
    # Schema configuration
    # --------------------------------------------------------------------------

    __tablename__ = 'User'

    # define table details
    email = Column(String(200), primary_key=True)
    password = Column(String(100))

    # define relationships
    events = relationship(
    	'Event',
    	secondary=user_has_event
    )
