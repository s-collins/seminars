import unittest
import datetime
from orm import Database

# ------------------------------------------------------------------------------
# Dictionaries for building test entities
# ------------------------------------------------------------------------------

TEST_EVENT = {
    'title' : "Simple Event",
    'description' : "A simple event for testing.",
    'date' : datetime.date(year=2019, month=1, day=1),
    'start_time' : datetime.time(hour=12, minute=0, second=0),
    'end_time' : datetime.time(hour=12, minute=0, second=0),
    'event_url' : 'simple_event.com',
    'image_url' : 'simple_event.com/images/image.jpg'   
}

TEST_LOCATION = {
    'name' : "Simple Location",
    'address' : "1234 Test Avenue",
    'city' : "City of Testville",
    'state' : "Ohio",
    'postcode' : "12345"   
}

TEST_SPEAKER_1 = {
    'first_name' : "John",
    'last_name' : "Doe",
    'credentials' : "John's credentials",
    'organization' : "John's organization"   
}

TEST_SPEAKER_2 = {
    'first_name' : "Sally",
    'last_name' : "Smith",
    'credentials' : "Sally's credentials",
    'organization' : "Sally's organization"   
}

# ------------------------------------------------------------------------------
# Event tests
# ------------------------------------------------------------------------------

class EventTestCase(unittest.TestCase):

    def setUp(self):
        self.db = Database.make_test_db()

    def test_save(self):
        # Construct event
        event = self.db.create_event(**TEST_EVENT)
        event.set_location(self.db.create_location(**TEST_LOCATION))

        # Save event
        self.db.save_event(event)

        # Load events from database
        all_events = self.db.load_all_events()

        # Test number of events
        self.assertEqual(1, len(all_events))

        # Test attributes of event
        expected_event = self.db.create_event(**TEST_EVENT)
        expected_location = self.db.create_location(**TEST_LOCATION)
        expected_event.location_name = expected_location.name
        e = all_events[0]
        self.assertEqual(expected_event, e)

    def test_save_also_saves_location(self):
        # Construct event
        event = self.db.create_event(**TEST_EVENT)
        event.set_location(self.db.create_location(**TEST_LOCATION))

        # Save event
        self.db.save_event(event)

        # Load location from database
        location = self.db.load_all_locations()[0]

        # Test location attributes
        self.assertEqual(self.db.create_location(**TEST_LOCATION), location)

    def test_save_event_with_existing_location(self):
        # Construct and save location
        location = self.db.create_location(**TEST_LOCATION)
        self.db.save_location(location)

        # Save multiple events with same location
        for i in range(4):
            event = self.db.create_event(**TEST_EVENT)
            event.set_location(self.db.create_location(**TEST_LOCATION))
            self.db.save_event(event)

        # Check database state
        self.assertEqual(4, len(self.db.load_all_events()))
        self.assertEqual(1, len(self.db.load_all_locations()))

    def test_save_also_saves_speakers(self):
        speakers = []
        speakers.append(self.db.create_speaker(**TEST_SPEAKER_1))
        speakers.append(self.db.create_speaker(**TEST_SPEAKER_2))

        # Construct event
        event = self.db.create_event(**TEST_EVENT)
        for speaker in speakers:
            event.add_speaker(speaker)

        # Save event
        self.db.save_event(event)

        saved_speakers = self.db.load_all_speakers()
        self.assertEqual(2, len(saved_speakers))


# ------------------------------------------------------------------------------
# Location tests
# ------------------------------------------------------------------------------

class LocationTestCase(unittest.TestCase):
    """
    TEST CASES:
        - save a location
    """

    def setUp(self):
        self.db = Database.make_test_db()

    def test_save(self):
        location = self.db.create_location(**TEST_LOCATION)
        self.db.save_location(location)

        # Test number of locations
        all_locations = self.db.load_all_locations()
        self.assertEqual(1, len(all_locations))

        # Test attributes of location
        expected_location = self.db.create_location(**TEST_LOCATION)
        l = all_locations[0]
        self.assertEqual(expected_location, l)

# ------------------------------------------------------------------------------
# Speaker test
# ------------------------------------------------------------------------------

class SpeakerTestCase(unittest.TestCase):

    def setUp(self):
        self.db = Database.make_test_db()

    def test_save(self):
        speaker = self.db.create_speaker(**TEST_SPEAKER_1)
        self.db.save_speaker(speaker)

        # Test number of speakers
        all_speakers = self.db.load_all_speakers()
        self.assertEqual(1, len(all_speakers))

        # Test attributes of speaker
        expected_speaker = self.db.create_speaker(**TEST_SPEAKER_1)
        s = all_speakers[0]
        self.assertEqual(expected_speaker, s)


if __name__ == '__main__':
    unittest.main()
