#import module of mysql connector

import mysql.connector

#create connection with mysql server

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database= "iot_sep2023"
)

#print(f"type={type(connection)}")

#create select query
# query1= "select * from temperatures;" 
query2="select * from students;"

#Create cursor through connection

cursor = connection.cursor()

#using cursor execute query
# cursor.execute(query1)
cursor.execute(query2)

#get all records from cursor(list)
# temp_list = cursor.fetchall()
stud_list = cursor.fetchall()

#display all temp on console
# print(temp_list)
# for record in temp_list:
#     print(record)
 
print(stud_list)
for(rollno,name,std,marks) in stud_list:
    # print(record)
    print(f"rollno={rollno},name ={name},std={std},marks={marks}")

#close the cursor
cursor.close()

#close the connection
connection.close()
