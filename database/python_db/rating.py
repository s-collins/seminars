from sqlalchemy import (Column, Integer, Enum)
from base import Base


class Rating(Base):
    __tablename__ = 'Rating'

    # Relation attributes
    id_rating = Column(Integer, primary_key=True)
    id_event = Column(Integer)
    stars = Column(Enum)

    def __init__(self, id_event, stars):
        self.id_event = id_event
        self.stars = stars
