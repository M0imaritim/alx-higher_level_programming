#!/usr/bin/python3
"""
Lists all states starting with N from database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                                 db=sys.argv[3], port=3306)

    curs = connection.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC;")
    states = curs.fetchall()

    for state in states:
        print(state)
    curs.close()
    connection.close()
