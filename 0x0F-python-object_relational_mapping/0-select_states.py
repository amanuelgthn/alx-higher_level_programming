#!/usr/bin/python3

"""
This script lists all states from the the database `hbtn_0e_0_usa`.
The script takes 3 arguments: mysql username, mysql password & database name
(no argument validation)
"""
import sys
import MySQLdb

if __name__ ==  "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    states = cur.fetchall()
    for item in states:
        print(item)
        db.commit()
        db.close()
