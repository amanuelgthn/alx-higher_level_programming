#!/usr/bin/python3
"""
-A script that lists all cities from the database hbtn_0e_4_usa
-script should take 3 arguments: mysql username, mysql password
and database name
-script should connect to a MySQL server running on localhost at port 3306
-Results must be sorted in ascending order by cities.id
-using only execute() once
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    query = """SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id ASC"""
    cur.execute(query)
    cities = cur.fetchall()
    for item in cities:
        print(item)
