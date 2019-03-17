from selenium import webdriver
from bs4 import BeautifulSoup
import logging
from time import sleep
from dateutil.parser import parse
import datetime
from .WrapperBase import WrapperBase

class Wrapper(WrapperBase):
	"""
	Scrapes 'Upcoming Seminars and Events' page from UA Department of
	Polymer Science site.
	"""

	NAME = 'The University of Akron, Department of Polymer Science'
	BASE_URL = 'https://uakron.edu/cpspe/news-events/calendar#!view/day/date/'

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
		return self.BASE_URL + datetime.datetime.today().strftime('%Y%m%d')

	def clean_text(self, text):
		return str(text.strip().encode('utf-8'))

	def extract_events(self):
		events = []

		# number of days forward (from today) to scrape
		num_days = 90
		
		day = datetime.datetime.today()
		for i in range(num_days):
			# update day
			day += datetime.timedelta(days=1)
			logging.info('Scraping page for ' + day.strftime('%Y-%m-%d'))

			# get HTML from URL
			url = self.BASE_URL + day.strftime('%Y%m%d')
			self.driver.get(url)
			sleep(.5)
			html = self.driver.execute_script('return document.body.innerHTML')
			soup = BeautifulSoup(html, features='html.parser')		

			# get events
			event_list = next(iter(soup.select('div#lw_cal_day_rightcol > div.lw_cal_event_list')), None)
			if event_list:
				event_trees = event_list.find_all(
					'div',
					{'class': lambda x: x and 'lw_tag_guest_speaker' in x.split()}
				)
				for tree in event_trees:
					event = self.__extract_event_from_tree(tree, day)
					events.append(event)
					logging.info(self.get_source_name() + ':Scraped event \"' + event.title + '\"')

		return events

	def __extract_event_from_tree(self, tree, date):
		fields = {}

		# get title
		title = next(iter(tree.select('div.lw_events_title')), None)
		if title:
			fields['title'] = self.clean_text(title.text)

		# get description
		description = next(iter(tree.select('div.lw_events_summary')), None)
		if description:
			fields['description'] = self.clean_text(description.text)

		# get date
		fields['date'] = date

		# get start_time
		start_time = next(iter(tree.select('span.lw_start_time')), None)
		if start_time:
			fields['start_time'] = parse(start_time.text.strip()).time()

		# get end_time
		end_time = next(iter(tree.select('span.lw_end_time')), None)
		if end_time:
			fields['end_time'] = parse(end_time.text.strip()).time()

		# get event_url
		event_url = next(iter(tree.select('div.lw_events_title > a')), None)
		if event_url:
			base_url = 'https://uakron.edu/cpspe/news-events/calendar'
			fields['event_url'] = base_url + event_url.get('href')

		# get image_url
		image_url = next(iter(tree.select('img.lw_image')), None)
		if image_url:
			fields['image_url'] = image_url.get('src')

		# get location!!!

		return self.db.create_event(**fields)


