from Base import DeclarativeBase
from Event_has_Speaker import event_has_speaker
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, Sequence
from sqlalchemy.orm import relationship


class Speaker(DeclarativeBase):

    # --------------------------------------------------------------------------
    # Schema configuration
    # --------------------------------------------------------------------------

    __tablename__ = 'Speaker'

    # Define table details
    speaker_id = Column(Integer, Sequence('speaker_id_seq'), primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    credentials = Column(String(200))
    organization = Column(String(200))

    # Define relationships
    events = relationship(
        'Event',
        secondary=event_has_speaker,
        back_populates='speakers'
    )

    # --------------------------------------------------------------------------
    # Methods
    # --------------------------------------------------------------------------

    def __eq__(self, other):
        return self.first_name == other.first_name and \
               self.last_name == other.last_name and \
               self.credentials == other.credentials and \
               self.organization == other.organization
