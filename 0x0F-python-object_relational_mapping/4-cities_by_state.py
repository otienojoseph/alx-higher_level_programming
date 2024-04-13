#!/usr/bin/python3
"""Script that returns list of cities from hbtn_0e_4_usa database"""

import sys
import MySQLdb


def listCities(user_name, password, db_name):
    db = MySQLdb.connect(user=user_name, passwd=password, db=db_name)
    cur = db.cursor()
    query = """
    SELECT * FROM cities
    ORDER BY id ASC
    """

    cur.execute(query)
    state_rows = cur.fetchall()

    for state in state_rows:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    [user_name, password, db_name] = sys.argv[1:]
    listCities(user_name, password, db_name)
