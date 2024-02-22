#!/usr/bin/python3
import MySQLdb
import sys

def listStates():
    [username, password, db_name] = sys.argv[1:]
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=db_name)
        # print("Connection successful")

        cur = db.cursor()
        cur.execute("USE %s" % db_name)
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cur.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to the MySQL database: ", e)

    finally:
        if 'db' in locals():
            cur.close()
            db.close()


if __name__ == "__main__":
    listStates()
