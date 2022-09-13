#!/usr/bin/python3

import sys
import MySQLdb

'''
Script that takes an argument and check for matching
'''

if __name__ == "__main__":
	db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

	mycursor = db.cursor()

	mycursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(sys.argv[4]))
	
	for i in mycursor.fetchall():
		print(i)

	mycursor.close()
	db.close()
