import paho.mqtt.client as mqtt
import utils.database as db

mqttc = mqtt.Client("Subscriber")

def on_connect(client,userdata,flags,rc):
    if rc ==0:
        print("Subscriber is added successfully")
        topic= "sensor/temperature"
        mqttc.subscribe(topic)
    else:
        print("subscriber is not added error code={rc}")

def on_message(client,userdata,message):
    print("Received message: "+str(message.payload)+ "on topic"+str(message.topic))
    temp= float(message.payload)
    print(f"Temperature = {temp}")
    query = f"insert into temperatures(temperature,location) values({temp},\"indrayani\");"
    db.execute_query(query)

mqttc.on_connect=on_connect
mqttc.on_message=on_message

host = "localhost"
mqttc.connect(host)

mqttc.loop_forever()