#!/usr/bin/python3
"""Script that lists a given name starting with specific letter"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    mycursor = db.cursor()
    mycursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    for i in mycursor.fetchall():
        print(i)

    mycursor.close()
    db.close()
