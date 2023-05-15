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

# Define the callback for handling received messages
def on_message(topic, message):
    print('Received message', message, 'on topic', topic)
    if message == b'on':
        led.on()
    elif message == b'off':
        led.off()

# Setup a GPIO Pin for the LED
led_pin = 2  # Replace with the GPIO pin connected to your LED
led = machine.Pin(led_pin, machine.Pin.OUT)

# Set the callback to the function on_message
mqtt_client.set_callback(on_message)

# Subscribe to a topic
topic = "your/topic"
mqtt_client.subscribe(topic)

print('Subscribed to topic')

# Wait for messages and handle them
while True:
    try:
        mqtt_client.wait_msg()
    except KeyboardInterrupt:
        print('Interrupted')
        mqtt_client.disconnect()
        break