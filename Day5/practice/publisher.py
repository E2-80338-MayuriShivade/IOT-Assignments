import paho.mqtt.client as mqtt

mqttc = mqtt.Client("Publisher")

def on_connect(client,userdata,flags,rc):
    if rc ==0:
        print("Publisher is added successfully")
    else:
        print("Publisher is not added Error code = {rc}")

def on_publish(client,userdata,mid):
    print("Message publish successfully")

mqttc.on_connect=on_connect
mqttc.on_publish=on_publish

host = "localhost"
mqttc.connect(host)

topic = "topic/hello"
payload = "HELLO DESD !!!!"
mqttc.publish(topic,payload)

mqttc.disconnect()