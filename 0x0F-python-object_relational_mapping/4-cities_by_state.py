#!/usr/bin/python3
'''
SQL joins in Python + Mysql
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

    mycursor.execute("SELECT cities.id, cities.name, states.name FROM states JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC")
    for i in mycursor.fetchall:
        print(i)
