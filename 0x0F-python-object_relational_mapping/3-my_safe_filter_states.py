#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                                 db=sys.argv[3], port=3306)
    curs = connection.cursor()
    curs.execute("SELECT * FROM states WHERE name = %s \
    ORDER BY states.id ASC;", (sys.argv[4], ))
    states = curs.fetchall()
    for state in states:
        print(state)
    curs.close()
    connection.close()
