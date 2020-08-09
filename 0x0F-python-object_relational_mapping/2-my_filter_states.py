#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa where
name matches the argument"""
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
    cur.execute("""SELECT * FROM states \
        WHERE name= '{}' ORDER BY id ASC""".format(sys.argv[4]))
    query_rows = cur.fetchall()

    # Print query
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)

    # Close cursor
    cur.close()
    conn.close()
