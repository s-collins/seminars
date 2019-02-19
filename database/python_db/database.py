from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

# Import all relations
from event import Event
from location import Location
from rating import Rating
from speaker import Speaker


class Database:

    def __init__(self, conn_string):
        self.conn_string = conn_string
        self.engine = create_engine(self.conn_string)
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


config = {
    'conn_string': 'sqlite:///:memory:'
}
db = Database(**config)
s1 = Speaker('Sean', 'Collins', 'programmer', 'UA')
s2 = Speaker('Megan', 'Collins', 'student', 'High School')

db.save(s1)
db.save(s2)

speakers = db.get_all_speakers()
for speaker in speakers:
    print(speaker.first_name, speaker.last_name)
