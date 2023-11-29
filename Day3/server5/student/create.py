import student.connection as db 

def insert_students(rollno,name,std,marks):
    conn = db.get_connection()

    query=f"insert into students values({rollno},\"{name}\",{std},{marks});"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

    cur.close()
    conn.close()

