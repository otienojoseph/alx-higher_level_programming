#!/usr/bin/python3

"""
    A script that lists all states with a name starting with 'N' from a 
    database hbtn_0e_0_usa username, password and database are given as args.
"""

import sys
import MySQLdb


def listStates(username, password, db_name):
    db = cur = None
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=db_name)
        # print("Connection successful")

        cur = db.cursor()
        cur.execute("USE %s" % db_name)
        cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
        states = cur.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to the MySQL database: ", e)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    try:
        [username, password, db_name] = sys.argv[1:]
        listStates(username, password, db_name)
    except ValueError as e:
        print("Usage: <function-name> user password db_name")
