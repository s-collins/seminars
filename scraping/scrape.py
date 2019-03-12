import database_settings
database_settings.config('mysql+pymysql://root:root@localhost/test_database')
import database

import cleveland_museum_of_art

if __name__ == '__main__':
	db = database.Database()

	scrapers = [
		cleveland_museum_of_art.Scraper()
	]

	all_events = []
	for scraper in scrapers:
		events = scraper.extract_events()
		for event in events:
			all_events.append(event)

	for e in all_events:
                # TODO: Save the location.........
		db.save_event(e)
