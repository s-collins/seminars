import database as db

TEST_DB = 'sqlite:///test.db'

if __name__ == '__main__':
    db.config(cnx_str=TEST_DB)

    test_db = db.Database()
    s1 = db.Speaker('Sean', 'Collins', 'programmer', 'UA')
    test_db.save(s1)

    print("Tests complete")
