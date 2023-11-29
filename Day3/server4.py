from flask import  Flask

#create server
app= Flask(__name__)

@app.route("/temp/<temp>")
def insert_temperature(temp):
    return f"Received temp : {temp}"

#run server
if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=3000,debug=True)
    app.run(debug=True)

# @app.route("/temp/<temp>")
# def insert_temperature():
#     return f"Received temperature={temp}"

