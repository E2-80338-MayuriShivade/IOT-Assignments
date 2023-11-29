#import flask
from flask import Flask
import utils.response as response
import utils.database as db

#create server
server=Flask(__name__)

@server.route("/welcome")
def welcome():
    return response.create_response("welcome to IOT Application")


@server.route("/temp", methods={'GET'})
def temperature_methods():
     #get data from DB
     query= f"select *  from temperatures;"

     #execute query to get temp from DB
     temps=db.execute_select_query(query)
     #return temps
     return response.create_response(temps)


server.run(debug=True)