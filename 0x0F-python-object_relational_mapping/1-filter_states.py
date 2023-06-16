#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    states = cur.fetchall()
    for item in states:
        if (item[1].startswith('N')):
            print(item)
