from Base import DeclarativeBase
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, Sequence
from sqlalchemy.orm import relationship


class Event(DeclarativeBase):
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
    location = relationship("Location", back_populates="events", lazy='joined')

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
