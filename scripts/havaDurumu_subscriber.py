#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Bağlandı, Result Code: " + str(rc))
    client.subscribe("hava_durumu") 

def on_message(client, userdata, msg):
    data = msg.payload.decode('utf-8')
    weather_data = json.loads(data)
    temperature = weather_data.get('temperature', None)
    if temperature:
        print(f"Anlık Hava Sıcaklığı: {temperature}°C")
    else:
        print("Hava sıcaklığı verisi alınamadı.")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)  

client.loop_forever()
