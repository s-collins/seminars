from sqlalchemy import (Column, String)
from tables.base import Base


class Location(Base):
    __tablename__ = 'Location'

    # Relation attributes
    name = Column(String, primary_key=True)
    details = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    postcode = Column(String)

    def __init__(self, name, details, address, city, state, postcode):
        self.name = name
        self.details = details
        self.address = address
        self.city = city
        self.state = state
        self.postcode = postcode
