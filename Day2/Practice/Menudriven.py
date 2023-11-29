import mysql.connector

connection = mysql.connector.connect(
      host = "localhost",
      port= 3306,
     user = "root",
     password = "root",
     database = "iot_sep2023")

def create():

 rollno= int(input("Enter rollno : "))
 name = input("Enter name : ")
 std = int(input("Enter std : "))
 marks = float(input("Enter marks : "))
 query = f"insert into students values({rollno},\"{name}\",{std},{marks});"

 cursor = connection.cursor()

 cursor.execute(query)
 
 connection.commit()

 cursor.close()
 connection.close()

def select():
 connection = mysql.connector.connect(
      host = "localhost",
      port= 3306,
     user = "root",
     password = "root",
     database = "iot_sep2023")

 query = f"select * from students;"
 cursor = connection.cursor()
 cursor.execute(query)
 stud_list = cursor.fetchall()

 for(rollno,name,std,marks) in stud_list:
  print(f"rollno={rollno},name=\"{name}\",std={std},marks={marks};")

  cursor.close()
  connection.close()

def update():
 connection = mysql.connector.connect(
      host = "localhost",
      port= 3306,
     user = "root",
     password = "root",
     database = "iot_sep2023")
 
 rollno= int(input("Enter rollno : "))
 marks = float(input("Enter marks : "))
 
 query = f"update students set marks={marks} where rollno={rollno};"

 cursor= connection.cursor()
 cursor.execute(query)
 connection.commit()
 cursor.close()
 connection.close()

def delete():
 connection = mysql.connector.connect(
      host = "localhost",
      port= 3306,
     user = "root",
     password = "root",
     database = "iot_sep2023")
 
 rollno= int(input("Enter roll no : "))
 query = f"delete from students where rollno = {rollno}"

 cursor = connection.cursor()
 cursor.execute(query)
 connection.commit()
 cursor.close()
 connection.close()
 
while(True):
 print("\nMenu :")
 print("1.Insert into database")
 print("2.Select database")
 print("3.update into database")
 print("4.delete from database")
 print("5.Exit")
 choice = int(input("Enter your choice : "))
 
       
 if choice == 1:
  create()
 elif choice == 2:
  select()
 elif choice ==3:
  update()
 elif choice == 4:
  delete()
 elif choice == 5:
   break
 else:
  print("invalid input")
  


   


  


