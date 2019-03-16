from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .Base import DeclarativeBase


class Location(DeclarativeBase):

    # --------------------------------------------------------------------------
    # Schema configuration
    # --------------------------------------------------------------------------

    __tablename__ = 'Location'

    # Define table details
    name = Column(String(100), primary_key=True)
    address = Column(String(200))
    city = Column(String(100))
    state = Column(String(100))
    postcode = Column(String(50))

    # Define relationships
    events = relationship("Event", back_populates="location")

    # --------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------- 

    def __repr__(self):
        """
        Specifies a format for representing the instance as a string.
        """
        frmt = (
            "<Location(\n"
            "\tname='%s'\n"
            "\taddress='%s'\n"
            "\tcity='%s'\n"
            "\tstate='%s'\n"
            "\tpostcode='%s'\n"
            ")>"
        )
        return frmt % (
            self.name,
            self.address,
            self.city,
            self.state,
            self.postcode
        )

    def __eq__(self, other):
        return self.name == other.name and \
               self.address == other.address and \
               self.city == other.city and \
               self.state == other.state and \
               self.postcode == other.postcode

