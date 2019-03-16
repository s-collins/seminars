from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Base import DeclarativeBase
from Event import Event
from Location import Location

def make_test_db():
    return Database('sqlite:///:memory:')

class Database():

    def __init__(self, cnx_str):
        self.engine = create_engine(cnx_str)
        self.Session = sessionmaker(bind=self.engine)

        # Create schema if it does not already exist
        DeclarativeBase.metadata.create_all(self.engine)

    def save_event(self, event):
        """
        Persists an event in the database, including the associated location.
        """
        sess = self.Session()
        sess.add(event)
        sess.commit()

    def load_all_events(self):
        """
        Queries the database for all saved events.
        """
        sess = self.Session()
        return sess.query(Event).all()
        sess.close()

    def save_location(self, location):
        """
        Persists a location in the database
        """
        sess = self.Session()
        sess.add(location)
        sess.commit()

    def load_all_locations(self):
        """
        Queries the database for all saved locations.
        """
        sess = self.Session()
        return sess.query(Location).all()
        sess.close()

    def load_unique_location(self, name):
        """
        Queries the database for a location with the given name.
        """
        sess = self.Session()

if __name__ == '__main__':
    location = Location(name = "Location 1")
    event = Event(title = "Event 1", description = "A test event",)
    event.location = location

    test_database = make_test_db()
    test_database.save(event)
