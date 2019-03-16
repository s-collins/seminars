import unittest
import Database
from Event import Event
from Location import Location
import datetime

def make_simple_test_event():
    return Event(
        title = "Simple Event",
        description = "A simple event for testing.",
        date = datetime.date(year=2019, month=1, day=1),
        start_time = datetime.time(hour=12, minute=0, second=0),
        end_time = datetime.time(hour=12, minute=0, second=0),
        event_url = 'simple_event.com',
        image_url = 'simple_event.com/images/image.jpg'
    )

def make_simple_test_location():
    return Location(
        name = "Simple Location",
        address = "1234 Test Avenue",
        city = "City of Testville",
        state = "Ohio",
        postcode = "12345"
    )

class EventTestCase(unittest.TestCase):

    def setUp(self):
        self.db = Database.make_test_db()

    def test_save(self):
        # Construct event
        event = make_simple_test_event()
        event.location = make_simple_test_location()

        # Save event
        self.db.save_event(event)

        # Load events from database
        all_events = self.db.load_all_events()

        # Test number of events
        self.assertEqual(1, len(all_events))

        # Test attributes of event
        expected_event = make_simple_test_event()
        expected_location = make_simple_test_location()
        e = all_events[0]
        self.assertEqual(1, e.event_id)
        self.assertEqual(expected_event.title, e.title)
        self.assertEqual(expected_event.description, e.description)
        self.assertEqual(expected_location.name, e.location_name)
        self.assertEqual(expected_event.date, e.date)
        self.assertEqual(expected_event.start_time, e.start_time)
        self.assertEqual(expected_event.end_time, e.end_time)
        self.assertEqual(expected_event.event_url, e.event_url)
        self.assertEqual(expected_event.image_url, e.image_url)
        self.assertEqual(expected_location, e.location)

    def test_save_also_saves_location(self):
        # Construct event
        event = make_simple_test_event()
        event.location = make_simple_test_location()

        # Save event
        self.db.save_event(event)

        # Load location from database
        location = self.db.load_all_locations()[0]

        # Test location attributes
        self.assertEqual(make_simple_test_location(), location)


class LocationTestCase(unittest.TestCase):
    """
    TEST CASES:
        - save a location
    """

    def setUp(self):
        self.db = Database.make_test_db()

    def test_save(self):
        # Construct location
        location = make_simple_test_location()

        # Save location
        self.db.save_location(location)

        # Load locations from database
        all_locations = self.db.load_all_locations()

        # Test number of locations
        self.assertEqual(1, len(all_locations))

        # Test attributes of location
        expected_location = make_simple_test_location()
        l = all_locations[0]
        self.assertEqual(expected_location, l)


if __name__ == '__main__':
    unittest.main()