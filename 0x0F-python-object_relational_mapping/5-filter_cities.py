#!/usr/bin/python3
'''
Takes an argument and searches from the table to list city names
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    mycursor = db.cursor()

    mycursor.execute("SELECT cities.name FROM states JOIN cities ON states.id = cities.state_id WHERE cities.name='{}' ORDER BY cities.id ASC".format([sys.argv[4]]))
    for i in mycursor.fetchall:
        if sys.argv[4] == states.name:
            print(i)
        else:
            print()
