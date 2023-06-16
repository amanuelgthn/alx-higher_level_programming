#!/usr/bin/python3
"""
A script that takes an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name ='{}' \
        ORDER BY id ASC;".format(sys.argv[4])
    cur.execute(query)
    states = cur.fetchall()
    for item in states:
        print(item)
