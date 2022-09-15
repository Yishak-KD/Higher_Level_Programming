#!/usr/bin/python3
"""A script that takes an argument and lists it's members"""

import sys
import MySQLdb

if __name__ == '__main__':
	db = MySQLdb.connect(
	user=sys.argv[1],
	passwd=sys.argv[2],
	db=sys.argv[3]
)
	mycursor = db.cursor()
	mycursor.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    AND states.name = '{:s}'\
                    ORDER BY cities.id ASC".format(sys.argv[4]))

	rows = cur.fetchall()

	new = []
	for i in rows:
		new.append(i[0])

	print(", ".join(new))

	mycursor.close()
	db.close()
