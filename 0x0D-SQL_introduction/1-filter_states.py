import sys
import MySQLdb

db = MySQLdb.connect(
    user='sys.argv[1]',
    passwd='sys.argv[2]',
    database='sys.argv[3]'
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
for i in mycursor.fetchall():
    print(i)
