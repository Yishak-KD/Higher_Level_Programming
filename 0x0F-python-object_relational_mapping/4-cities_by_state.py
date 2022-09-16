#!/usr/bin/python3
"""Script that lists all cities froma given database"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    mycursor = db.cursor()
    mycursor.execute("SELECT cities.id, cities.name, states.name\
    FROM states JOIN cities\
    ON cities.state_id = states.id\
    ORDER BY cities.state_id ASC")
    for i in mycursor.fetchall():
        print(i)

    mycursor.close()
    db.close()
