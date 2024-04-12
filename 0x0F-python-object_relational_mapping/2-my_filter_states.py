#!/usr/bin/python3
"""Script that returns list of states from hbtn_0e_0_usa database"""

import sys
import MySQLdb


def listStates(user_name, password, db_name, state):
    """Script that returns all states whose names match state"""
    db = MySQLdb.connect(user=user_name, passwd=password, db=db_name)
    cur = db.cursor()
    query = """
    SELECT * FROM states
    WHERE name LIKE BINARY '{}'
    ORDER BY id ASC
    """.format(
        state
    )

    cur.execute(query)
    state_rows = cur.fetchall()

    for state in state_rows:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    [user_name, password, db_name, state] = sys.argv[1:]
    listStates(user_name, password, db_name, state)
