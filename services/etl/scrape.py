from wrappers import ClevelandMuseumOfArt
from wrappers import UADepartmentOfPolymerScience
from wrappers import SiegalLifelongLearning
from orm import Database
import logging


# Configure logging format
logging.basicConfig(level=logging.INFO, format='%(message)s')


if __name__ == '__main__':
	database = Database.Database('mysql+pymysql://root:root@db:3306/events')
	#database = Database.make_test_db()

	# List of wrapper objects for data sources
	all_wrappers = [
		SiegalLifelongLearning.Wrapper(database),
		ClevelandMuseumOfArt.Wrapper(database),
		UADepartmentOfPolymerScience.Wrapper(database),
	]

	# Extract events from each data source
	for wrapper in all_wrappers:

		name = wrapper.get_source_name()
		url = wrapper.get_url()

		logging.info('-' * 80)
		logging.info(name)
		logging.info(url)
		logging.info('-' * 80)

		if wrapper.ping(url):
			logging.info('Successful ping')
			events = wrapper.extract_events()
			logging.info('Scraped ' + str(len(events)) + ' events')
			for event in events:
				database.save_event(event)
		else:
			logging.info('Connection Failure')

