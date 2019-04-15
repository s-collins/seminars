import datetime
import logging
from .WrapperBase import WrapperBase
from .ScraperUtil import ScraperUtil


class Wrapper(WrapperBase):
	"""
	Scrapes 'Upcoming Events' page for Siegal Lifelong Learning series
	(Case Western Reserve University)
	"""

	NAME = 'Siegal Lifelong Learning'
	URL = 'https://case.edu/lifelonglearning/lectures-and-events/upcoming-events'

	def __init__(self, db):
		self.db = db
		self.helper = ScraperUtil()

	def get_source_name(self):
		return self.NAME

	def get_url(self):
		return self.URL

	def extract_events(self):
		html = self.helper.GetHTML(self.URL)
		event_trees = self.helper.CssSelectMultiple(html, 'div.mb-20')

		if (len(event_trees) == 0):
			return []

		events = []
		for tree in event_trees:
			event = self.__extract_event_from_tree(tree)
			events.append(event)
			logging.info('Scraped event \"' + event.title + '\"')

		return events

	def __extract_event_from_tree(self, tree):
		h = self.helper
		fields = {}

		# get title
		title = h.CssSelectFirst(tree, 'div.views-field-title')
		if title:
			fields['title'] = h.GetText(title)

		# get date
		date = h.CssSelectFirst(tree, 'span.views-field-field-course-date')
		try:
			fields['date'] = datetime.datetime.strptime(h.GetText(date), '%A, %B %d, %Y')
		except: pass

		# get event_url
		event_url = h.CssSelectFirst(tree, 'div.views-field-title > h3 > a')
		if event_url:
			base_url = 'http://case.edu'
			fields['event_url'] = base_url + h.GetAttribute(event_url, 'a', 'href')

		# get description
		if event_url:
			html = h.GetHTML(fields['event_url'])
			description = h.CssSelectFirst(html, 'div.field--name-field-course-description > p')
			if description:
				fields['description'] = h.GetText(description)

		return self.db.create_event(**fields)
