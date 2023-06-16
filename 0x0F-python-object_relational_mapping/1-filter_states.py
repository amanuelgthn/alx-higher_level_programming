#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from hbtn_0e_0_usa
"""
import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', passwd='root',
                    db='hbtn_0e_0_usa', port=3306)
cur = db.cursor()
cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
states = cur.fetchall()
for item in states:
    if (item[1].startswith('N')):
        print(item)
db.commit()
db.close()
