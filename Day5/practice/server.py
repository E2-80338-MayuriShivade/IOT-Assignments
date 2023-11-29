from flask import Flask,request,jsonify

import paho.mqtt.client as mqtt

mqttc = mqtt.Client("Publisher")

server= Flask(__name__)

@server.route("/temperature",methods = {'POST'})
def add_temperature():
    temp = request.form.get('temperature')
    loc = request.form.get('location')
    
    d=dict()
    if float(temp) >= 35.0:
        mqttc.connect("localhost")
        mqttc.publish("room/fan","ON")
        mqttc.disconnect()
        d={
           "status":"success",
           "fan status":"ON"
        }

    else:
        mqttc.connect("localhost")
        mqttc.publish("room/fan","OFF")
        mqttc.disconnect()
        d={
            "status":"Success",
            "fan status":"OFF"
        }   
    return jsonify(d)

server.run(debug=True)     
