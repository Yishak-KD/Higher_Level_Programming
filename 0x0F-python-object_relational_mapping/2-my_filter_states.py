#!/usr/bin/python3
"""Script that takes an argument and check for matching"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    mycursor = db.cursor()

    mycursor.execute(
        "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(sys.argv[4]))

    for i in mycursor.fetchall():
        print(i)

    mycursor.close()
    db.close()
