import paho.mqtt.client as mqtt

#create instance of client class
mqttc = mqtt.Client("Subscriber")

#define all callbacks
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Subscriber is connected successfully")
        #subscribe for topic
        topic= "topic/hello"
        mqttc.subscribe(topic)
    else:
        print(f"Subscriber is not connected Error code :{rc}")


def on_message(client, userdata, message):
    print(f"Recieved msg : \"{message.payload}\"on topic \"{message.topic}\"")
mqttc.on_connect = on_connect
mqttc.on_message = on_message    

#connect with broker
host = "localhost"
mqttc.connect(host)

mqttc.loop_forever()
