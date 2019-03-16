from wrappers import ClevelandMuseumOfArt
from wrappers import UADepartmentOfPolymerScience
from orm import Database
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

if __name__ == '__main__':
	database = Database.make_test_db()

	# List of wrapper objects for data sources
	all_wrappers = [
		#ClevelandMuseumOfArt.Wrapper(database),
		UADepartmentOfPolymerScience.Wrapper(database),
	]

	for wrapper in all_wrappers:
		# get name of data source
		source = wrapper.get_source_name()

		if wrapper.ping(wrapper.get_url()):

			# report successful connection
			logging.info(source + ':Successful ping')

			# extract events
			events = wrapper.extract_events()
			logging.info(source + ':Scraped ' + str(len(events)) + ' events')

			# save events to database
			for event in events:
				database.save_event(event)

		else:
			logging.info(source + ':Failed ping')
