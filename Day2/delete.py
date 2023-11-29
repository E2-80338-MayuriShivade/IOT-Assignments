#import mysql

import mysql.connector

#create connection with mysql server
connection = mysql.connector.connect(
      host = "localhost",
      port = 3306,
      user ="root",
      password = "root",
      database = "iot_sep2023"
      )
#delete query
rollno = int(input("Enter rollno :"))
loc = input("Enter location :")

query1 = f"delete from students where rollno={rollno};"
query2 = f"delete from temperatures where location= \"{loc}\";"

#create cursor
cursor = connection.cursor()

#execute
cursor.execute(query1)
cursor.execute(query2)

#commit
connection.commit()

#close cursor
cursor.close()

#close connection
connection.close()