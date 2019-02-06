import requests
import threading
import time
import paho.mqtt.client as mqtt




# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

def pinger():
    while(True):
        try:
            requests.get('http://localhost/mongodb')
            client.publish('GSN1',"Server is solid")
        except:
            client.publish('GSN1',"Error at server1")
        time.sleep(10)

client.connect("broker.mqttdashboard.com", 1883, 60)
t=threading.Thread(target=pinger)
t.start()
client.loop_forever()
