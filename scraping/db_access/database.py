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

    def __init__(self, first_name, last_name, credentials, organization):
        self.id_speaker = None
        self.first_name = first_name
        self.last_name = last_name
        self.credentials = credentials
        self.organization = organization

    def __str__(self):
        output = 'Speaker:' \
               + '\n\tid_speaker: {0}'.format(self.id_speaker) \
               + '\n\tfirst_name: {0}'.format(self.first_name) \
               + '\n\tlast_name: {0}'.format(self.last_name) \
               + '\n\tcredentials: {0}'.format(self.credentials) \
               + '\n\torganization: {0}'.format(self.organization)
        return output


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

    def get_all_speakers(self):
        results = self.session.query(Speaker).all()
        return results
