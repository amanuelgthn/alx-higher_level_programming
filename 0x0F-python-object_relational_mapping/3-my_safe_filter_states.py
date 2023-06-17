#!/usr/bin/python3
"""
A script that takes in arguments and displays all calues in the states
table of hbtn_0e_0_usa where the name matches the argument and
that is safe from MySQL injections.
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT * FROM states WHERE name = %s"""
    name = format(sys.argv[4]).encode('utf-8')
    0x0F-python-object_relational_mapping
    states = cur.fetchall()
    for item in states:
        print(item)
