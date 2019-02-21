import unittest
import sqlite3
import os

TEST_DATABASE = 'test_database.db'

import database_settings

class SpeakerTests(unittest.TestCase):

    def setUp(self):
        # Create a test database
        file = open('/resources/schema.sql', 'r')
        data_definition = file.read()
        conn = sqlite3.connect(TEST_DATABASE)
        cursor = conn.cursor()
        cursor.executescript(data_definition)
        conn.commit()
        cursor.close()
        conn.close()
        file.close()

        # Create database and connect to the test database
        database_settings.config('sqlite:///{}'.format(TEST_DATABASE))
        import database
        self.db = database.Database()

    def tearDown(self):
        os.remove(TEST_DATABASE)

    def test_speakers_are_saved(self):
        import database

        s1 = database.Speaker('Bill', 'Gates', 'American business magnate', 'Microsoft')
        s2 = database.Speaker('Steve', 'Jobs', 'American business magnate', 'Apple')
        self.db.save_speaker(s1)
        self.db.save_speaker(s2)
        speakers = self.db.get_all_speakers()

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


if __name__ == '__main__':
    unittest.main()