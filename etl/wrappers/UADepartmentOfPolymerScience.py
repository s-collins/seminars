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

	def get_source_name(self):
		return self.NAME

	def get_url(self):
		return self.URL

	def extract_events(self):
		events = []

		soup = self.get_soup(self.get_url())
		print(soup)
		event_trees = soup.select('div.lw_events_day')
		print(len(event_trees))
		for tree in event_trees:
			print("scraping event")
			event = self.__extract_event_from_tree(tree)
			events.append(event)
			logging.info(self.get_source_name() + ':Scraped event \"' + event.title + '\"')

		return events

	def __extract_event_from_tree(self, tree):
		fields = {}

		# get event URL
		event_url = next(iter(tree.select('a')), None)
		if event_url:
			fields['event_url'] = event_url.text.strip()

			event_soup = self.get_soup(fields['event_url'])

			# get title
			title = next(iter(event_soup.select('#lw_cal_events > h1')), None)
			if title:
				fields['title'] = title.test.strip()
				print(fields['title'])
