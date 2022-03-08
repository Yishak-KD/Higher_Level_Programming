#!/usr/bin/python3

"""
Script that lists all the names that starts with a specific alphabet
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    my_cursor = db.cursor()

    my_cursor.execute("SELECT *
                      FROM states
                      WHERE name LIKE '{}'
                      ORDER BY id ASC".format(sys.argv[4]))
    for m in my_cursor.fetchall():
        print(m)
