import practice.utils.connection as conn

def execute_query(query):
    connection =  connection.get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

# def execute_select_query(query):
#     connection = connection.get_connection()   
