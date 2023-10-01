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
    cur.execute("SELECT * FROM cities RIGHT JOIN states ON cities.state_id =\
    states.id WHERE states.name = '{}'".format(sys.argv[4]))
    table = cur.fetchall()

    """ Output the result """
    print(", ".join([retval[2] for retval in table]))
    cur.close()
