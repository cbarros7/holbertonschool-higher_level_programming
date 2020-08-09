#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    # Start cursor
    cur = conn.cursor()
    # Query
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities, states WHERE cities.state_id = states.id\
                ORDER BY cities.id ASC")
    query_rows = cur.fetchall()

    # Print query
    for row in query_rows:
        print(row)

    # Close cursor
    cur.close()
    conn.close()
