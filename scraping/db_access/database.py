from sqlalchemy import Column, Date, Integer, String, Time
from sqlalchemy.orm import sessionmaker

import database_settings as settings
engine = settings.get_engine()
Base = settings.get_base()

# TABLES

class Event(Base):
    __tablename__ = 'Event'
    __table_args__ = {'autoload': True}


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

    def save_speaker(self, s):
        filter = {'first_name': s.first_name, 'last_name': s.last_name}
        speakers = self.get_speaker(filter)
        for speaker in speakers:
            if s.duplicates(speaker):
                raise RuntimeError("Duplicate speaker")
        self.session.add(s)
        self.session.commit()

    def get_speaker(self, filter):
        return self.session.query(Speaker).filter_by(**filter).all()

    def get_all_speakers(self):
        return self.session.query(Speaker).all()
