import database_settings as db_settings
import sqlite3

# Variables
TEST_DB = 'test.db'

def create_test_db():
    query = open('/resources/schema.sql', 'r').read()
    connection = sqlite3.connect(TEST_DB)
    c = connection.cursor()
    c.executescript(query)
    connection.commit()
    c.close()
    connection.close()
    

if __name__ == '__main__':
    create_test_db()

    # Configure the settings for the database module
    db_settings.config('sqlite:///{0}'.format(TEST_DB))
    from database import Database, Speaker

    # Create the data access layer
    db = Database()

    s1 = Speaker('Sally', 'Smith', 'student', 'UA')
    s2 = Speaker('Bob', 'Smith', 'student', 'UA')

    db.session.add_all([s1, s2])
    db.session.commit()

    speakers = db.get_all_speakers()
    print(speakers[0])
    print(speakers[1])
