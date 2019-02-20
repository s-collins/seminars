from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import all relations
from tables.base import Base
from tables.event import Event
from tables.location import Location
from tables.rating import Rating
from tables.speaker import Speaker

# Settings
CONNECTION_STR = ''

# Configuration
def config(cnx_str):
    global CONNECTION_STR
    CONNECTION_STR = cnx_str


class Database:

    def __init__(self):
        self.engine = create_engine(CONNECTION_STR)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def save(self, entity):
        session = self.Session()
        session.add(entity)
        session.commit()
        session.close()

    def get_all_speakers(self):
        session = self.Session()
        return session.query(Speaker).all()
