from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from Base import DeclarativeBase
from Event import Event
from Location import Location
from Speaker import Speaker


def make_test_db():
    return Database('sqlite:///:memory:')


class Database():

    def __init__(self, cnx_str):
        self.engine = create_engine(cnx_str)
        self.Session = sessionmaker(bind=self.engine)
        self.sess = self.Session()

        # Create schema if it does not already exist
        DeclarativeBase.metadata.create_all(self.engine)

    def __del__(self):
        self.sess.flush()
        self.sess.close()

    # --------------------------------------------------------------------------
    # Factory methods
    #
    #  - These factory methods prevent duplication in database.
    #  - Entities (e.g., Event, Location, etc.) should not be constructed
    #    directly
    #
    # --------------------------------------------------------------------------

    def create_event(self, **kwargs):
        """
        Constructs an event (without location)
        """
        return Event(**kwargs)

    def create_location(self, **kwargs):
        """
        If location does not already exist in database, constructs the location.
        Otherwise, returns the existing location.
        """
        location = self.load_location(kwargs['name'])
        if location is None:
            return Location(**kwargs)
        return location

    def create_speaker(self, **kwargs):
        """
        If speaker with given first name, last name, and organization is not
        already in the database, constructs the speaker.
        Otherwise, returns the existing speaker.
        """
        try:
            result = self.sess.query(Speaker).filter_by(
                first_name = kwargs['first_name'],
                last_name = kwargs['last_name'],
                organization = kwargs['organization']
            ).one()
            return result
        except NoResultFound:
            return Speaker(**kwargs)

    # --------------------------------------------------------------------------
    # Save entities
    # --------------------------------------------------------------------------

    def save_event(self, event):
        self.sess.add(event)
        self.sess.commit()

    def save_location(self, location):
        self.sess.add(location)
        self.sess.commit()

    def save_speaker(self, speaker):
        self.sess.add(speaker)
        self.sess.commit()

    # --------------------------------------------------------------------------
    # Load entities
    # --------------------------------------------------------------------------   

    def load_all_events(self):
        return self.sess.query(Event).all()

    def load_all_locations(self):
        return self.sess.query(Location).all()

    def load_all_speakers(self):
        return self.sess.query(Speaker).all()

    def load_location(self, name):
        try:
            result = self.sess.query(Location).filter_by(name=name).one()
            return result
        except NoResultFound:
            return None


