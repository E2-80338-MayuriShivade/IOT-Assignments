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
    

#create insert query
rollno = int(input("Enter rollno: "))
name = input("Enter name :")
std = int(input("Enter std :"))
marks = float(input("Enter marks:"))

#for temperature
temperature = float(input("Enter temperature : "))
location = input("Enter Location : ")

query1 = f"insert into students values({rollno},\"{name}\",{std},{marks});"
query2= f"insert into temperatures(temperature,location) values({temperature},\"{location}\");"

#create cursor using connection
cursor = connection.cursor()

#execute query
cursor.execute(query1)
cursor.execute(query2)

#update changes 
connection.commit()
 
#close the cursor
cursor.close()

#close the connection
connection.close()