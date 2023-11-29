#import flask
from flask import Flask , request
import utils.response as response
import utils.database as db

server=Flask(__name__)

@server.route("/welcome")
def welcome():
    return response.create_response("welcome to IOT Application")


@server.route("/temp", methods={'GET','POST','PUT','DELETE'})
def temperature_methods():
    if(request.method =='GET'):
        #get data from DB
        query= f"select *  from temperatures;"

        #execute query to get temp from DB
        temps=db.execute_select_query(query)
       #return temps
        return response.create_response(temps)
    elif(request.method=='POST'):
        temp = request.get_json().get('temperature')
        loc = request.get_json().get('location')

        query=f"insert into temperatures(temperature,location) values({temp},\"{loc}\");"
        db.execute_query(query)

        return response.create_response("succesfully added")
    
    
     
        #print(f"temp={temp},loc={loc}")
    elif(request.method=='PUT'):
        temp = request.get_json().get('temperature')
        loc = request.get_json().get('location')
        query = f"update temperatures set temperature={temp} where location=\"{loc}\";"
        db.execute_query(query)
        return response.create_response("succesfully added")
    
    elif(request.method=='DELETE'):
        loc = request.get_json().get('location')
        query = f"delete from temperatures where location = \"{loc}\";"
        db.execute_query(query)
        return response.create_response("deleted successfully")


server.run(debug=True)
