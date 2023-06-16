#!/usr/bin/python3

"""
This script creates a table called `song` in the database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', port=3306, passwd='root',db='hbtn_0e_0_usa')
cur = db.cursor()

# Create the database if it doesn't already exist
cur.execute("CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa")

# Drop the `song` table if it already exists
cur.execute("DROP TABLE IF EXISTS song")

# Create the `song` table
cur.execute("CREATE TABLE song ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )")

# Get a list of songs
songs = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')

# Insert each song into the `song` table
for song in songs:
    cur.execute("INSERT INTO song (title) VALUES(%s)", (song,))
    print("Auto Increment ID: %s" % cur.lastrowid)

# Commit the changes to the database
db.commit()

# Close the database connection
db.close()