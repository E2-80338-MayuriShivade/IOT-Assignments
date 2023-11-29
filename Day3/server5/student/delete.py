import student.connection as db

def delete_student(rollno):
    conn = db.get_connection()

    query = f"delete from students where rollno={rollno};"
    cur=conn.cursor()
    cur.execute(query)
    conn.commit()

    cur.close()
    conn.close()

