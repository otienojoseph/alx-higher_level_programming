#!/usr/bin/python3
"""Script that returns list of cities from hbtn_0e_4_usa database"""

import sys
import MySQLdb


def listCities(user_name, password, db_name, state_name):
    try:
        db = MySQLdb.connect(user=user_name, passwd=password, db=db_name)
        cur = db.cursor()
        query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

        cur.execute(query, (state_name,))
        city_rows = cur.fetchall()

        print(", ".join([city[0] for city in city_rows]))

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <db name> <state name>")

    [user_name, password, db_name, state_name] = sys.argv[1:]
    listCities(user_name, password, db_name, state_name)
