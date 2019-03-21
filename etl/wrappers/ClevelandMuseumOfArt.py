import datetime_glob
import re
import logging
from .WrapperBase import WrapperBase
from .ScraperUtil import ScraperUtil


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
        self.helper = ScraperUtil()

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

            html = self.helper.GetHTML(page_url)
            event_trees = self.helper.CssSelectMultiple(html, 'div.cma-views-row')

            if (len(event_trees) == 0):
                break

            for tree in event_trees:
                event = self.__extract_event_from_tree(tree)
                event.set_location(location)
                events.append(event)           
                logging.info('Scraped event \"' + event.title + '\"')

            page_index += 1

        return events

    def __extract_event_from_tree(self, tree):
        h = self.helper
        fields = {}

        # get title
        title = h.CssSelectFirst(tree, 'div.views-field-title > a')
        if title:
            fields['title'] = h.GetText(title)

        # get description
        description = h.CssSelectFirst(tree, 'div.views-field-field_event_description')
        if description:
            fields['description'] = h.GetText(description)

        # get date
        date = h.CssSelectFirst(tree, 'span.date-display-start')
        if date:
            date = h.GetAttribute(date, 'span', 'content')
            fields['date'] = self.date_matcher.match(date).as_date()

        # get start time
        start_time = h.CssSelectFirst(tree, 'span.date-display-start')
        if start_time:
            start_time = h.GetAttribute(start_time, 'span', 'content')
            fields['start_time'] = self.date_matcher.match(start_time).as_time()

        # get end time
        end_time = h.CssSelectFirst(tree, 'span.date-display-end')
        if end_time:
            end_time = h.GetAttribute(end_time, 'span', 'content')
            fields['end_time'] = self.date_matcher.match(end_time).as_time()

        # get URLs
        event_url = h.CssSelectFirst(tree, 'div.views-field-title > a')
        if event_url:
            # get event URL
            event_url_tail = h.GetAttribute(event_url, 'a', 'href')
            fields['event_url'] = 'https://www.clevelandart.org' + event_url_tail

            # get image URL
            html = h.GetHTML(fields['event_url'])
            banner = h.CssSelectFirst(html, 'div.pane-views-panes')
            if banner:
                image_element = h.CssSelectFirst(banner, 'img')
                image_url = h.GetAttribute(image_element, 'img', 'src')
                if image_url:
                    fields['image_url'] = h.GetText(image_url)

        return self.db.create_event(**fields)
