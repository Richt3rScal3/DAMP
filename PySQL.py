import mysql.connector

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="dan",         # your username
                     passwd="test1", # your password
                     auth_plugin='mysql_native_password',  # your password auth
                     db="test")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
print(cur)
# Use all the SQL you like
#cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
#for row in cur.fetchall():
#    print row[0]
#
db.close()