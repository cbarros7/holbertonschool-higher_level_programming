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
    cur.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            WHERE states.name=%s", (sys.argv[4], ))

    query_rows = cur.fetchall()
    out = []
    for row in query_rows:
        out.append(row[0])
    # Print query
    print(', '.join(out))

    # Close cursor
    cur.close()
    conn.close()
