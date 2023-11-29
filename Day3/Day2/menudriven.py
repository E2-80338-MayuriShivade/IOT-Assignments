import mysql.connector

#create function
def create():
 connection = mysql.connector.connect(
     host = "localhost",
     port = 3306,
     user = "root",
     password = "root",
     database= "iot_sep2023"
)
 rollno =int(input("Enter roll no : "))
 name = input("Enter name : ")
 std = int(input("Enter std :"))
 marks= float(input("Enter marks:"))

 query= f"insert into students values({rollno},\"{name}\",{std},{marks});"

 cursor = connection.cursor()
 cursor.execute(query)
 connection.commit()
 cursor.close()
 connection.close()

def update():
 connection=mysql.connector.connect(
     host="localhost",
     port=3306,
     user="root",
     password="root",
     database="iot_sep2023"
    )
 name = input("Enter name of student: ")
 marks = input("Enter updated marks: ")

 query= f"update students set marks={marks} where name=\"{name}\";"
 cursor = connection.cursor()
 cursor.execute(query)
 connection.commit()
 cursor.close()
 connection.close()

def delete():
  connection=mysql.connector.connect(
     host="localhost",
     port=3306,
     user="root",
     password="root",
     database="iot_sep2023"
 )
  rollno=int(input("Enter rollno:"))

  query = f"delete from students where rollno={rollno};"

  cursor=connection.cursor()
  cursor.execute(query)
  connection.commit()
  cursor.close()
  connection.close()



while True:
    print("\nMENU")
    print("1.Insert data into database")
    print("2.Update database")
    print("3.Delete record from database") 
    print("4.Exit")
    choice=int(input("Enter your choice : "))

    if choice==1:
     create()
    elif choice==2:
     update()
    elif choice==3:
     delete()
    elif choice==4:
     break
    else:
     print("Invalid input")  
   
# def exit():
#   return 1


  




