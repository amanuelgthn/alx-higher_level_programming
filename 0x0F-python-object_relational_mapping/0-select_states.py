#!/usr/bin/python3

"""
This script lists all states from the the database `hbtn_0e_0_usa`.
The script takes 3 arguments: mysql username, mysql password & database name
(no argument validation)
"""
import MySQLdb

db = MySQLdb.connect(host='localhost', user='aman', passwd='AAaa222!!',
                    db='hbtn_0e_0_usa', port=3306)
cur = db.cursor()
cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
states = cur.fetchall()
for item in states:
    print(item)
db.commit()
db.close()
