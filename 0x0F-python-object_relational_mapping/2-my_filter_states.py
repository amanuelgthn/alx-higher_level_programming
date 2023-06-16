#!/usr/bin/python3
"""

"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    format_query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(sys.argv[4])
    cur.execute(format_query)
    states = cur.fetchall()
    for item in states:
        print(item)
