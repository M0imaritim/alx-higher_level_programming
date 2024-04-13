#!/usr/bin/python3
"""module gets all states from datbase"""

import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                                 db=sys.argv[3], port=3306)
    curs = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}%' \
              ORDER BY states.id ASC;".format(sys.argv[4])
    curs.execute(query)
    states = curs.fetchall()
    for state in states:
        print(state)
