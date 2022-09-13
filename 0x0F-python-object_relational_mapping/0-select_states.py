#!/usr/bin/python3

import sys
import MySQLdb

'''
A script that list all states from a given database
'''

if __name__ == '__main__':

	db = MySQLdb.connect(
    	user=sys.argv[1],
    	passwd=sys.argv[2],
	db=sys.argv[3]
	)

	mycursor = db.cursor()

	mycursor.execute("SELECT * FROM states ORDER BY id ASC")
	
	rows = mycursor.fetchall()
	for i in rows:
		print(i)
	
	mycursor.close()
	db.close()
