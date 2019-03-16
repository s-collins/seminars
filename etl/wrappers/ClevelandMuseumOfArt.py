import datetime_glob
import re
from .WrapperBase import WrapperBase
from orm.Database import Database


class Wrapper(WrapperBase):
    """
    Scrapes lectures page for The Cleveland Museum of Art.
    """

    NAME = 'The Cleveland Museum of Art'
    URL = 'https://www.clevelandart.org/events/lectures'
    LOCATION_DICT = {
        'name': 'The Cleveland Museum of Art',
        'address': '11150 East Boulevard',
        'city': 'Cleveland',
        'state': 'Ohio',
        'postcode': '44106'
    }

    def __init__(self):
        self.date_matcher = datetime_glob.Matcher(pattern='%Y-%m-%dT%H:%M:%S-*')

    def get_source_name(self):
        return self.NAME

    def get_url(self):
        return self.URL

    def extract_events(self):
    	pass
