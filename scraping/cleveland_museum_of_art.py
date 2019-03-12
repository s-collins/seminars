import scraper_base
import datetime_glob
import re
import database


class Scraper(scraper_base.ScraperBase):
    """
    Scrapes lectures page for The Cleveland Museum of Art.
    """

    URL = 'https://www.clevelandart.org/events/lectures'
    LOCATION = database.Location(
        name='The Cleveland Museum of Art',
        address='11150 East Boulevard',
        city='Cleveland',
        state='Ohio',
        postcode='44106'
    )

    def __init__(self):
        self.date_matcher = datetime_glob.Matcher(pattern='%Y-%m-%dT%H:%M:%S-*')

    def get_url(self):
        return URL

    def extract_events(self):
        soup = scraper_base.get_soup(self.URL)
        view_rows = soup.find_all('div', class_='views-row')
        events = []
        for row in view_rows:
            try:
                title = self.__get_title(row)
                description = self.__get_description(row)
                date, start_time, end_time = self.__get_date_and_times(row)
                event_url = self.__get_event_url(row)
            except:
                continue
            events.append(database.Event(title, description, LOCATION, date, start_time, end_time, event_url))
        return events

    def __get_title(self, view_row):
        title_field = view_row.find('div', {'class': 'views-field-title'})
        title_text = title_field.find('a').text
        return title_text

    def __get_description(self, view_row):
        description_field = view_row.find('div', {'class':'views-field-field_event_description'})
        return description_field.text

    def __get_date_and_times(self, view_row):
        start_element = view_row.findChildren('span', {'class': 'date-display-start'})[0]['content']
        end_element = view_row.findChildren('span', {'class': 'date-display-end'})[0]['content']
        date = self.date_matcher.match(start_element).as_date()
        start_time = self.date_matcher.match(start_element).as_time()
        end_time = self.date_matcher.match(end_element).as_time()
        return date, start_time, end_time

    def __get_event_url(self, view_row):
        base_url = 'https://www.clevelandart.org'
        url_extension = view_row.find('div', {'class': 'views-field-title'}).find('a').get('href')
        return base_url + url_extension

    #def __get_location_details(self, view_row, event_url):
        #soup = scraper_base.get_soup(event_url)
        #location_details = soup.select('div.field-name-field-location-details')[0].text
        #return location_details
