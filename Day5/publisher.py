#import mqtt module 
import paho.mqtt.client as mqtt

#create instance of client class
mqttc = mqtt.Client("Publisher")

#define all required callbacks
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Publisher is connected successfully")
    else:
        print(f"Publisher is not connected Error code :{rc}")

def on_publish(client,userdata,mid):
    print("Message is published successfully")

#register call back function with our client instance
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish     

#connect with broker
host = "localhost"
mqttc.connect(host)

#publish message
topic = "topic/hello"
payload = "Hello Python MQTT"
mqttc.publish(topic,payload)

#disconnect from broker8
mqttc.disconnect()

