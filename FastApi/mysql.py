import pymysql.cursors
import pymysql

db = MySQLdb.connect(host="localhost:50306",    # your host, usually localhost
                     user="root",         # your username
                     passwd="samoel123",  # your password
                     db="samoca")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = db.cursor()

# Use all the SQL you like
sql =("SELECT * FROM students")

cursor.execute(sql, ('webmaster@python.org',))
result = cursor.fetchone()
print(result)
   
db.close()