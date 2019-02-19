import mysql.connector

credentials = {
    'user': 'app',
    'password': 'app',
    'host': 'db',
    'database': 'app',
    'raise_on_warnings': True
}

# Continue attempting to connect until successful
while True:
    try:
        cnx = mysql.connector.connect(**credentials)
        cursor = cnx.cursor()
        cursor.execute("CREATE TABLE Person (name CHAR(100))")
        cursor.close()
        cnx.commit()
        cnx.close()
        break
    except mysql.connector.Error as err:
        pass
