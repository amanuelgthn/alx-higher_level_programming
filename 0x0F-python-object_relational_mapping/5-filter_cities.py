#!/usr/bin/python3
"""
-A script that takes in the name of a state as an argument and lists all cities
-takes 4 arguments:mysql username, mysql password, database name
and state name (SQL injection free!)
-Connects to MySQL server running on localhost at port 3306
-Results are sorted in ascending order by cities.id
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT cities.name FROM cities\
        JOIN states\
            ON cities.state_id = states.id\
            WHERE BINARY states.name = %s\
            ORDER BY cities.id ASC;"""
    name = format(sys.argv[4]).encode('utf-8')
    cur.execute(query, (name,))
    states = cur.fetchall()
    i = 0
    for item in states:
        if (i == len(states) - 1):
            print('{}'.format(item[0]))
            continue
        print('{}'.format(item[0]), end=", ")
        i += 1
