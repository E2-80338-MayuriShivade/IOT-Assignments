#Import module of flask
from flask import Flask
#flask:module Flask:class

#create server object using Flask
server = Flask(__name__)

@server.route("/")                     #REST API --"/ : decorator"
def homepage():
    return "This is Home page"

@server.route("/welcome")              #REST API
def welcome():
    return "WELCOME TO THE WORLD OF IOT"

@server.route("/test")
def test():
    return "This is for testing"

#run  your server contineuosly
server.run()                           #http://127.0.0.1:5000  : IP address(127.0.0.1):port number(5000)

