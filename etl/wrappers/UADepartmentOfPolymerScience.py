from selenium import webdriver
from bs4 import BeautifulSoup
import logging
from time import sleep
from dateutil.parser import parse
from .WrapperBase import WrapperBase

class Wrapper(WrapperBase):
	"""
	Scrapes 'Upcoming Seminars and Events' page from UA Department of
	Polymer Science site.
	"""

	NAME = 'The University of Akron, Department of Polymer Science'
	URL = 'https://www.uakron.edu/dps/seminars'

	def __init__(self, db):
		self.db = db

		ops = webdriver.ChromeOptions()
		ops.add_argument('--headless')
		ops.add_argument('--no-sandbox')
		ops.add_argument('--disable-dev-shm-usage')
		self.driver = webdriver.Chrome(chrome_options=ops)
		self.driver.implicitly_wait(20)

	def __del__(self):
		self.driver.quit()

	def get_source_name(self):
		return self.NAME

	def get_url(self):
		return self.URL

	def get_soup(self, url):
		self.driver.get(url)
		sleep(5)
		html = self.driver.execute_script('return document.body.innerHTML')
		soup = BeautifulSoup(html, features='html.parser')
		return soup


	def extract_events(self):
		events = []

		soup = self.get_soup(self.get_url())

		event_days = soup.select('div.lw_events_day')
		for day in event_days:
			event_trees = day.select('span.lw_events_title')
			for tree in event_trees:
				event = self.__extract_event_from_tree(tree)
				events.append(event)
				logging.info(self.get_source_name() + ':Scraped event \"' + event.title + '\"')

		return events

	def clean_text(self, text):
		return str(text.strip().encode('utf-8'))

	def __extract_event_from_tree(self, tree):
		fields = {}

		# get event URL
		event_url = next(iter(tree.select('a')), None)
		if event_url:
			fields['event_url'] = event_url.get('href').strip()
			soup = self.get_soup(fields['event_url'])

			# get title
			title = soup.find('div', {'id': 'lw_cal_events'}).h1
			if title:
				fields['title'] = self.clean_text(title.text)

			# get description
			description = next(iter(soup.select('div.lw_calendar_event_description')), None)
			if description:
				fields['description'] = self.clean_text(description.find('p').text)

			# get date
			date = soup.find('h5', {'id': 'lw_cal_this_day'}).text
			if date:
				fields['date'] = parse(date).date()

			# get start time
			start_time = next(iter(soup.select('span.lw_start_time')), None)
			if start_time:
				fields['start_time'] = parse(start_time.text.strip()).time()

			# get end time
			end_time = next(iter(soup.select('span.lw_end_time')), None)
			if end_time:
				fields['end_time'] = parse(end_time.text.strip()).time()

			# get image url
			left_column = soup.find('div', {'id': 'lw_cal_event_leftcol'})
			image_url = next(iter(left_column.select('img')), None)
			if image_url:
				fields['image_url'] = image_url.get('src').strip()

		return self.db.create_event(**fields)

