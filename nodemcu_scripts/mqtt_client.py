import machine
import network
import time
from umqtt.simple import MQTTClient

# Setup the wifi connection
ssid = "your_wifi_ssid"
password = "your_wifi_password"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Connect to your wifi
wifi.connect(ssid, password)

# Wait until the board is connected to the WiFi
while not wifi.isconnected():
    time.sleep(1)
    print('Waiting for connection...')

print('Connected to WiFi')

# Setup the MQTT client
broker_address = "your_broker_address"
client_id = "your_client_id"
mqtt_client = MQTTClient(client_id, broker_address)

# Connect to your MQTT broker
mqtt_client.connect()

print('Connected to MQTT broker')

# Publish a message to a topic
topic = "your/topic"
message = "Hello, MQTT!"
mqtt_client.publish(topic, message)

print('Published a message')

# Remember to call disconnect when finished
mqtt_client.disconnect()