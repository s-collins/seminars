import Base
from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy import Sequence


class Location(Base.DeclarativeBase):
    __tablename__ = 'Location'

    # Define table details
    name = Column(String(100), primary_key=True)
    address = Column(String(200))
    city = Column(String(100))
    state = Column(String(100))
    postcode = Column(String(50))

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
