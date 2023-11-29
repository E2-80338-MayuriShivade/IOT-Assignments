from flask import Flask,render_template,request
 
server = Flask(__name__)

@server.route("/",methods = {'GET'})
def welcome():
    temp = 35.0
    return render_template("welcome.html",message=temp)

@server.route("/temp" ,methods={'GET'})
def read_temperatures():
    #read all temps from database
    temps = [(32.0,"Nira"),(35.5,"Indrayani"),(36.7,"pravara")]

    return render_template("table.html",message=temps)

@server.route("/temperature",methods = {'GET','POST'})
def add_temperature():
    if request.method == 'POST':
        temp =request.form.get("temp")
        loc = request.form.get("loc")
        print(f"Temp={temp},location={loc}")
        return f"Temp={temp},location={loc}"
    
    return render_template("form.html")


server.run(debug=True)

