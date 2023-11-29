import paho.mqtt.client as mqtt

mqttc = mqtt.Client("Subscriber")

def on_connect(client,userdata,flags,rc):
    if rc ==0:
        print("Subscriber is added")
        topic="topic/hello"
        mqttc.subscribe(topic)
    else:
        print("subscriber is not connected error code ={rc}") 

def on_message(client,userdata,message):
    print(f"Received message : \"{message.payload}\" on topic \"{message.topic}\"")  

mqttc.on_connect=on_connect
mqttc.on_message=on_message

host = "localhost"
mqttc.connect(host)

mqttc.loop_forever()