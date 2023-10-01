#!/usr/bin/python3
"""script that takes in an argument and display."""


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
    cur.execute("SELECT DISTINCT * FROM states WHERE name LIKE \
            '{}' ORDER BY id LIMIT 1".format(sys.argv[4]))
    table = cur.fetchall()

    """ Output the result """
    for row in table:
        print(row)

    cur.close()
    conn.close()
