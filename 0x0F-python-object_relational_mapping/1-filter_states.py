#!/usr/bin/python3

import sys
import MySQLdb

'''
Script that lists a given name starting with specific letter'''

if __name__ == "__main__":
	db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
	charset="utf8"
    )
	mycursor = db.cursor()
	mycursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
	
	for i in mycursor.fetchall():
		print(i)

	mycursor.close()
	db.close()
