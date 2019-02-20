import unittest
import database as db
from sqlalchemy.engine import reflection
from sqlalchemy import types


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        TEST_CONNECTION_STR = 'sqlite:///test.db'
        db.config(TEST_CONNECTION_STR)
        self.db = db.Database()
        self.inspector = reflection.Inspector.from_engine(self.db.engine)


class DatabaseHasCorrectTableNames(DatabaseTest):
    def runTest(self):
        TABLES = [
            'Event',
            'Location',
            'Rating',
            'Speaker',
            'Event_has_Speaker'
        ]
        tables = self.inspector.get_table_names()
        self.assertEqual(set(TABLES), set(tables))


class CorrectEventTable(DatabaseTest):
    def runTest(self):
        columns = self.inspector.get_columns('Event')

        # Verify 'id_event'
        column = next((c for c in columns if c['name'] == 'id_event'))
        self.assertEqual(type(column['type']), types.INTEGER)
        self.assertEqual(column['primary_key'], True)
        self.assertEqual(column['nullable'], False)
        self.assertEqual(column['autoincrement'], 'auto')

        # Verify 'title'
        column = next((c for c in columns if c['name'] == 'title'))
        self.assertEqual(type(column['type']), types.VARCHAR)
        self.assertEqual(column['primary_key'], False)
        self.assertEqual(column['nullable'], False)

        # TODO: remove after finishing test implementation
        self.assertTrue(False, "\n\n***TEST IS NOT FULLY IMPLEMENTED\n")


if __name__ == '__main__':
    unittest.main()
