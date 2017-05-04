#!/usr/bin/python

import MySQLdb
# Open database connection
db = MySQLdb.connect("127.0.0.1","root","Lmy19940219","trade_analysis" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
#sql = "INSERT INTO trade_analysis VALUES ('value1', 'value2', 'value3', 'v4','v5','v6','v7','v8');"
sql = "delete from trade_analysis where title = 'value111';"
#sql = "INSERT into trade_analysis SELECT 'value111', 'value2', 'value3', 'v4','v5','v6','v7','v8' FROM DUAL where not exists (select Title from trade_analysis where Title = 'value111');"
#sql += "where not exists (select Title from trade_analysis where Title = 'value11');"



try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

#print(cursor.execute(sql))
# disconnect from server
db.close()
