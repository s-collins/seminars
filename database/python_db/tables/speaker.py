from sqlalchemy import (Column, Integer, String)
from tables.base import Base


class Speaker(Base):
    __tablename__ = 'Speaker'

    # Relation attributes
    id_speaker = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    credentials = Column(String)
    organization = Column(String)

    def __init__(self, first_name, last_name, credentials, organization):
        self.first_name = first_name
        self.last_name = last_name
        self.credentials = credentials
        self.organization = organization
