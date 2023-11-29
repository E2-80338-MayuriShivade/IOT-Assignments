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

#create update query 
name = input("Enter name of student : ")
marks = input("Enter updated marks: ")

loc = input("Enter location :")
temp = input("Enter updated temperature: ")

query1= f"update students set marks={marks} where name = \"{name}\";"
query2 = f"update temperatures set temperature={temp} where location=\"{loc}\";"


#create cursor
cursor = connection.cursor()

#execute cursor
cursor.execute(query1)
cursor.execute(query2)

#commit your changes
connection.commit()

#close cursor
cursor.close()

#close the connection
connection.close()