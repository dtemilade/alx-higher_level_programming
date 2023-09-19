#!/usr/bin/python3
"""script that lists all states from the database"""


import MySQLdb
import sys


if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

""" Establishing connection """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        conn=database_name
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
    ORDER BY states.id ASC")
    table = cur.fetchall()

""" Output the result """
    for row in table:
        print(row)
    cur.close()
    conn.close()
