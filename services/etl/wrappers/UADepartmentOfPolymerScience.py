import logging
from dateutil.parser import parse
import datetime
from .WrapperBase import WrapperBase
from .ScraperUtil import ScraperUtil

class Wrapper(WrapperBase):
	"""
	Scrapes 'Upcoming Seminars and Events' page from UA Department of
	Polymer Science site.
	"""

	NAME = 'The University of Akron, Department of Polymer Science'
	BASE_URL = 'https://uakron.edu/cpspe/news-events/calendar#!view/day/date/'

	def __init__(self, db):
		self.db = db
		self.helper = ScraperUtil()

	def get_source_name(self):
		return self.NAME

	def get_url(self):
		return self.BASE_URL + datetime.datetime.today().strftime('%Y%m%d')

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

			# extract node containing list of events
			html = self.helper.GetHTML(url)
			selector = 'div#lw_cal_day_rightcol > div.lw_cal_event_list'
			event_list = self.helper.CssSelectFirst(html, selector)

			# skip this day if no event list was found
			if event_list is None:
				continue

			# extract event nodes
			tag = 'div'
			css_class = 'lw_tag_guest_speaker'
			event_trees = self.helper.SelectElementsMulticlass(event_list, tag, css_class)

			# extract event from each node
			for tree in event_trees:
				event = self.__extract_event_from_tree(tree, day)
				events.append(event)
				logging.info('Scraped event \"' + event.title + '\"')

		return events

	def __extract_event_from_tree(self, tree, date):
		h = self.helper
		fields = {}

		# get title
		title = h.CssSelectFirst(tree, 'div.lw_events_title')
		if title:
			fields['title'] = h.GetText(title)

		# get description
		description = h.CssSelectFirst(tree, 'div.lw_events_summary')
		if description:
			fields['description'] = h.GetText(description)

		# get date
		fields['date'] = date.strftime('%Y-%m-%d')

		# get start_time
		start_time = h.CssSelectFirst(tree, 'span.lw_start_time')
		if start_time:
			start_time = h.GetText(start_time)
			fields['start_time'] = parse(start_time).time()

		# get end_time
		end_time = h.CssSelectFirst(tree, 'span.lw_end_time')
		if end_time:
			end_time = h.GetText(end_time)
			fields['end_time'] = parse(end_time).time()

		# get event_url
		event_url = h.CssSelectFirst(tree, 'div.lw_events_title > a')
		if event_url:
			base_url = 'https://uakron.edu/cpspe/news-events/calendar'
			fields['event_url'] = base_url + h.GetAttribute(event_url, 'a', 'href')

		# get image_url
		image_url = h.CssSelectFirst(tree, 'img.lw_image')
		if image_url:
			fields['image_url'] = h.GetAttribute(image_url, 'img', 'src')

		# save event
		event = self.db.create_event(**fields)

		# get location
		location = h.CssSelectFirst(tree, 'div.lw_events_location')
		if location:
			location_fields = {'name': h.GetText(location)} 
			location = self.db.create_location(**location_fields)
			self.db.save_location(location)
			event.set_location(location)

		return event
