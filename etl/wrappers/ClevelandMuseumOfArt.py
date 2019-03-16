import datetime_glob
import re
from .WrapperBase import WrapperBase

import logging


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

    def __init__(self, db):
        self.date_matcher = datetime_glob.Matcher(pattern='%Y-%m-%dT%H:%M:%S-*')
        self.db = db

    def get_source_name(self):
        return self.NAME

    def get_url(self):
        return self.URL

    def extract_events(self):
        location = self.db.create_location(**self.LOCATION_DICT)
        events = []

        page_index = 0
        while True:
            page_url = self.get_url() + '?page=' + str(page_index)
            soup = self.get_soup(page_url)
            event_trees = soup.select('div.cma-views-row')
            for tree in event_trees:
                event = self.__extract_event_from_tree(tree)
                event.set_location(location)
                events.append(event)           
                logging.info(self.get_source_name() + ':Scraped event \"' + event.title + '\"')
            page_index += 1
            if (len(event_trees) == 0):
                break

        return events

    def __extract_event_from_tree(self, tree):
        fields = {}

        # get title
        title = next(iter(tree.select('div.views-field-title > a')), None)
        if title:
            fields['title'] = title.text.strip()

        # get description
        description = next(iter(tree.select('div.views-field-field_event_description')), None)
        if description:
            fields['description'] = description.text.strip()

        # get date
        date = next(iter(tree.select('span.date-display-start')), None)
        if date:
            fields['date'] = self.date_matcher.match(date['content']).as_date()

        # get start time
        start_time = next(iter(tree.select('span.date-display-start')), None)
        if start_time:
            fields['start_time'] = self.date_matcher.match(start_time['content']).as_time()

        # get end time
        end_time = next(iter(tree.select('span.date-display-end')), None)
        if end_time:
            fields['end_time'] = self.date_matcher.match(end_time['content']).as_time()

        # get URLs
        event_url = next(iter(tree.select('div.views-field-title > a')), None)
        if event_url:
            # get event URL
            fields['event_url'] = ('https://www.clevelandart.org' + event_url.get('href')).strip()

            # get image URL
            event_soup = self.get_soup(fields['event_url'])
            banner = next(iter(event_soup.select('div.pane-views-panes')), None)
            if banner:
                image_url = next(iter(banner.select('img')), None).get('src')
                if image_url:
                    fields['image_url'] = image_url.strip()

        return self.db.create_event(**fields)