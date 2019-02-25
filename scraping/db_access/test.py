import unittest
import sqlite3
import os
import database_settings

TEST_DATABASE = 'test_database.db'

def setup_test_database():
    # create empty test database
    file = open('/resources/schema.sql', 'r')
    data_definition = file.read()
    conn = sqlite3.connect(TEST_DATABASE)
    cursor = conn.cursor()
    cursor.executescript(data_definition)
    conn.commit()
    cursor.close()
    conn.close()
    file.close()   

    # Create database instance and connect to test database
    database_settings.config('sqlite:///{}'.format(TEST_DATABASE))
    import database
    return database.Database()

def teardown_test_database():
    os.remove(TEST_DATABASE)

class SpeakerTests(unittest.TestCase):

    def setUp(self):
        self.db = setup_test_database()

    def tearDown(self):
        teardown_test_database()

    def test_speakers_are_saved(self):
        import database

        s1 = database.Speaker('Bill', 'Gates', 'American business magnate', 'Microsoft')
        s2 = database.Speaker('Steve', 'Jobs', 'American business magnate', 'Apple')
        self.db.save_speaker(s1)
        self.db.save_speaker(s2)
        speakers = self.db.get_speakers()

        # check number of speakers
        self.assertEqual(2, len(speakers))

        # check first speaker
        self.assertEqual(speakers[0].id_speaker, 1)
        self.assertEqual(speakers[0].first_name, 'Bill')
        self.assertEqual(speakers[0].last_name, 'Gates')
        self.assertEqual(speakers[0].credentials, 'American business magnate')
        self.assertEqual(speakers[0].organization, 'Microsoft')

        # check first speaker
        self.assertEqual(speakers[1].id_speaker, 2)
        self.assertEqual(speakers[1].first_name, 'Steve')
        self.assertEqual(speakers[1].last_name, 'Jobs')
        self.assertEqual(speakers[1].credentials, 'American business magnate')
        self.assertEqual(speakers[1].organization, 'Apple')           

    def test_duplicates_same_organization(self):
        """Speakers are duplicates iff same name AND same organization."""
        import database
        s1 = database.Speaker('Bill', 'Gates', 'American business magnate', 'Microsoft')
        s2 = database.Speaker('Bill', 'Gates', 'American business magnate', 'Microsoft')
        self.db.save_speaker(s1)
        with self.assertRaises(RuntimeError):
            self.db.save_speaker(s2)

    def test_duplicates_no_organization(self):
        import database
        s1 = database.Speaker('Bill', 'Gates', 'American business magnate', 'Microsoft')
        s2 = database.Speaker('Bill', 'Gates')
        self.db.save_speaker(s1)
        with self.assertRaises(RuntimeError):
            self.db.save_speaker(s2)


class LocationTests(unittest.TestCase):
    
    def setUp(self):
        self.db = setup_test_database()

    def tearDown(self):
        teardown_test_database()

    def test_location_is_saved(self):
        import database

        # create a location
        attributes = {
            'name': 'Cleveland-Marshall College of Law',
            'details': 'college',
            'address': '1801 Euclid Ave',
            'city': 'Cleveland',
            'state': 'Ohio',
            'postcode': 44115
        }
        l1 = database.Location(**attributes)

        # save the location
        self.db.save_location(l1)

        # read all locations
        locations = self.db.get_locations()

        # check number of locations
        self.assertEqual(1, len(locations))

        # check location
        self.assertEqual(locations[0].name, 'Cleveland-Marshall College of Law')
        self.assertEqual(locations[0].details, 'college')
        self.assertEqual(locations[0].address, '1801 Euclid Ave')
        self.assertEqual(locations[0].city, 'Cleveland')
        self.assertEqual(locations[0].state, 'Ohio')
        self.assertEqual(locations[0].postcode, '44115')

    def test_duplicates(self):
        import database
        l1 = database.Location(name='TestLocation')
        l2 = database.Location(name='TestLocation')
        self.db.save_location(l1)
        with self.assertRaises(RuntimeError):
            self.db.save_location(l2)


if __name__ == '__main__':
    unittest.main()
