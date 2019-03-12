from sqlalchemy import Column, Date, Integer, String, Time
from sqlalchemy.orm import sessionmaker

import database_settings as settings
engine = settings.get_engine()
Base = settings.get_base()

# TABLES

class Event(Base):
    __tablename__ = 'Event'
    __table_args__ = {'autoload': True}

    def __init__(self, title, description, location, date, start_time, end_time, url):
        self.id_event = None
        self.title = title
        self.description = description
        self.location = location
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.url = url


class Speaker(Base):
    __tablename__ = 'Speaker'
    __table_args__ = {'autoload': True}

    def __init__(self, first_name, last_name, credentials=None,
                 organization=None):
        self.id_speaker = None
        self.first_name = first_name
        self.last_name = last_name
        self.credentials = credentials
        self.organization = organization

    def duplicates(self, speaker):
        if self.first_name != speaker.first_name:
            return False
        if self.last_name != speaker.last_name:
            return False
        if self.organization is None or speaker.organization is None:
            return True
        if self.organization == speaker.organization:
            return True 
        return False


class Location(Base):
    __tablename__ = 'Location'
    __table_args__ = {'autoload': True}

    def __init__(self, name, address=None, city=None, state=None, postcode=None):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.postcode = postcode


class Rating(Base):
    __tablename__ = 'Rating'
    __table_args__ = {'autoload': True}


class Event_has_Speaker(Base):
    __tablename__ = 'Event_has_Speaker'
    __table_args__ = {'autoload': True}

# DATABASE

class Database:

    def __init__(self):
        self.engine = engine
        self.metadata = Base.metadata
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save_event(self, e):
        try:
            self.session.add(e)
            self.session.commit()
        except:
            self.session.rollback()
            raise RuntimeError("Error saving event")

    def save_location(self, l):
        try:
            self.session.add(l)
            self.session.commit()
        except:
            self.session.rollback()
            raise RuntimeError("Error saving location")

    def save_speaker(self, s):
        filter = {'first_name': s.first_name, 'last_name': s.last_name}
        speakers = self.get_speakers(filter)
        for speaker in speakers:
            if s.duplicates(speaker):
                raise RuntimeError("Duplicate speaker")
        self.session.add(s)
        self.session.commit()

    def get_locations(self, filter=None):
        if filter is None:
            return self.session.query(Location).all()
        return self.session.query(Location).filter_by(**filter).all()

    def get_speakers(self, filter=None):
        if filter is None:
            return self.session.query(Speaker).all()
        return self.session.query(Speaker).filter_by(**filter).all()
