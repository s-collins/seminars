from Base import DeclarativeBase
from Event_has_Speaker import event_has_speaker
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, Sequence
from sqlalchemy.orm import relationship


class Event(DeclarativeBase):

    # --------------------------------------------------------------------------
    # Schema configuration
    # --------------------------------------------------------------------------

    __tablename__ = 'Event'

    # Define table details
    event_id = Column(Integer, Sequence('event_id_seq'), primary_key=True)
    title = Column(String(500))
    description = Column(String)
    location_name = Column(String(100), ForeignKey('Location.name'))
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    event_url = Column(String)
    image_url = Column(String)

    # Define relationships
    location = relationship(
        "Location",
        back_populates="events",
        lazy='joined'
    )
    speakers = relationship(
        "Speaker",
        secondary=event_has_speaker,
        back_populates='events'
    )

    # --------------------------------------------------------------------------
    # Methods
    # --------------------------------------------------------------------------

    def add_speaker(self, speaker):
        self.speakers.append(speaker)

    def set_location(self, location):
        self.location = location

    def __repr__(self):
        """
        Specifies a format for representing the instance as a string.
        """
        frmt = (
            "<Event(\n"
            "\tevent_id='%s' \n"
            "\ttitle='%s' \n"
            "\tdescription='%s' \n"
            "\tlocation_name='%s' \n"
            "\tdate='%s' \n"
            "\tstart_time='%s' \n"
            "\tend_time='%s' \n"
            "\tevent_url='%s' \n"
            "\timage_url='%s'\n"
            ")>"
        )
        return frmt % (
            self.event_id,
            self.title,
            self.description,
            self.location_name,
            self.date,
            self.start_time,
            self.end_time,
            self.event_url,
            self.image_url
        )

    def __eq__(self, other):
        return self.title == other.title and \
               self.description == other.description and \
               self.location_name == other.location_name and \
               self.date == other.date and \
               self.start_time == other.start_time and \
               self.end_time == other.end_time and \
               self.event_url == other.event_url and \
               self.image_url == other.image_url
                   