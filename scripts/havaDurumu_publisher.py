#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import json
import time
import requests

def get_current_temperature():
    api_key = 'c64af769e2124617aa1214415230612' 
    city = 'Ankara'  
    url = f'http://api.weatherapi.com/v1/current.json?key=c64af769e2124617aa1214415230612&q=ankara&aqi=no'

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        current_weather = weather_data.get('current', None)
        if current_weather:
            current_temperature = current_weather.get('temp_c', None)
            return current_temperature
        else:
            return "Hava durumu verisi bulunamadı."
    else:
        return "Hava durumu verileri alınamadı."

def on_publish(client, userdata, mid):
    print("Mesaj yayınlandı.")

client = mqtt.Client()
client.on_publish = on_publish

client.connect("test.mosquitto.org", 1883, 60) 

while True:
    temperature_data = get_current_temperature()
    if isinstance(temperature_data, float) or isinstance(temperature_data, int):
        payload = json.dumps({"temperature": temperature_data})
        client.publish("hava_durumu", payload, qos=1)  
    else:
        print(temperature_data)
    time.sleep(5)  

