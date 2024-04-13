#!/usr/bin/python3
"""
 takes in the name of a state as an argument and lists all
 cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                                 db=sys.argv[3], port=3306)
    curs = connection.cursor()
    curs.execute("SELECT cities.name FROM cities JOIN states ON \
    cities.state_id = states.id WHERE states.name = %s;",
                 (sys.argv[4], ))
    cities = curs.fetchall()
    print(", ".join(city[0] for city in cities))
    curs.close()
    connection.close()
