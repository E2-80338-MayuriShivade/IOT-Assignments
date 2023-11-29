from flask import Flask , request

import student.create
import student.read
import student.update
import student.delete

app = Flask(__name__)

@app.route("/student",methods = {'POST'})
#retrive data from form
def add_student():
    rollno=request.form.get('rollno')
    name=request.form.get('name')
    std=request.form.get('std')
    marks=request.form.get('marks')
    
    #insert data insto DB
    student.create.insert_students(rollno,name,std,marks)

    #return some response to the client
    return "Student is Added successfully in DB"
    
@app.route("/student",methods={'GET'})
def read_students():
    studs = student.read.get_students()

    print("Student list: \n")
    for stud in studs:
        print(stud)

    return studs  

@app.route("/student",methods= {'PUT'})  
def update_student():
    rollno= request.form.get('rollno')
    marks= request.form.get('marks')

    student.update.update_student(rollno,marks)

    return "student updated successfully"

@app.route("/student", methods={'DELETE'})
def delete_student():
    rollno = request.form.get('rollno')
    student.delete.delete_student(rollno)
    
    return "student deleted successfully"

app.run(debug=True)