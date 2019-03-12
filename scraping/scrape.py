import database_settings
database_settings.config('mysql+pymysql://root:root@localhost/test_database')
import database

import cleveland_museum_of_art

if __name__ == '__main__':
    db = database.Database()

    scrapers = [
        cleveland_museum_of_art.Scraper()
    ]

    for scraper in scrapers:
        events = scraper.extract_events()
        for event in events:
            db.save_location(scraper.LOCATION)
            db.save_event(event)
