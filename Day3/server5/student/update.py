import student.connection as db

def update_student(rollno,marks):
    conn = db.get_connection()

    query = f"update students set marks={marks} where rollno={rollno};"
    cur = conn.cursor()
    cur.execute(query)

    conn.commit()
    cur.close()
    conn.close()

