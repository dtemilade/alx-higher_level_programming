#!/usr/bin/python3
"""script that lists all cities from the database"""


import MySQLdb
import sys


if __name__ == "__main__":

    """ Establishing connection """
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306)
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
         LEFT JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    table = cur.fetchall()

    """ Output the result """
    for row in table:
        print(row)

    cur.close()
    conn.close()
