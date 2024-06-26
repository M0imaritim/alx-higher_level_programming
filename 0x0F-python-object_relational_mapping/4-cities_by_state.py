#!/usr/bin/python3
"""module lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                                 db=sys.argv[3], port=3306)
    curs = connection.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;")
    cities = curs.fetchall()

    for city in cities:
        print(city)
