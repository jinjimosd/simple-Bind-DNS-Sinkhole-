#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("10.15.181.112","dnssinkhole","password","DomainServer" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM domains"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]

      # Now print fetched result
      print (fname)
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()