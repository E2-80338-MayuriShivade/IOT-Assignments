
import database.connection as db

def get_temperature():
    connection= db.get_connection()
    
    query=f"select * from temperatures;"

    cursor = connection.cursor()
    cursor.execute(query)
    temps=cursor.fetchall()
    connection.commit()

    cursor.close()
    connection.close()
    return temps
