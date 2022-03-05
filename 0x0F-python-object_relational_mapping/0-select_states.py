#!/usr/bin/python3
"""
Script that prints all the lists from a given databases
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )
    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM states ORDER BY id ASC")
    for i in mycursor.fetchall():
        print(i)
