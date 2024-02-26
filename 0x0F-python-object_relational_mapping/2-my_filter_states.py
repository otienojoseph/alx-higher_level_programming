#!/usr/bin/python3

"""
    A script that takes a list of arguments and displays all values
    in the states table of hbtn_0e_0_usa
    where name matches the argument
    username, password, database and state_name are given as args.
"""

import sys
import MySQLdb


def listStates(username, password, db_name, state_name):
    db = cur = ""
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=db_name)

        cur = db.cursor()
        cur.execute("USE {}".format(db_name))
        cur.execute("""SELECT * FROM states
                    WHERE name LIKE BINARY '{}'
                    ORDER BY id ASC""".format(state_name))
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
        [username, password, db_name, state_name] = sys.argv[1:]
        listStates(username, password, db_name, state_name)
    except ValueError as e:
        print("Usage: <function-name> user password db_name state_name")
