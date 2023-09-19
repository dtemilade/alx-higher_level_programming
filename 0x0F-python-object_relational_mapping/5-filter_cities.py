#!/usr/bin/python3
"""script that lists all cities from the database"""


import MySQLdb
import sys


if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

""" Establishing connection """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        conn=database_name
    )
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 LEFT JOIN states\
                 ON states.id = cities.state_id\
                 WHERE states.name LIKE BINARY (%s) ORDER BY cities.id ASC",
                (state_name,))
    table = cur.fetchall()

    end_str = ""
    str_cities = ""

""" Output the result """
    for row in table:
        str_cities = str_cities + end_str + row[0]
        end_str = ", "

    print(str_cities)
    cur.close()
    conn.close()
