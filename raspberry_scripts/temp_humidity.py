import paho.mqtt.client as mqtt
from RPi_GPIO_i2c_LCD import lcd
import time

# MQTT parameters
SERVER = '192.168.1.22'  # MQTT Server Address (Change to the IP address of your Pi)
TOPIC = 'temp_humidity'

# Initialize the LCD
def MyFunction(self):
    self.lcd.display_string("Waiting for data...",2)

lcdDisplay = lcd.HD44780(0x27, MyFunction)
lcdDisplay.set("Temperature/Humidity:",1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    temp_humidity = msg.payload.decode('utf-8')  # Convert the message to string
    temp, humidity = temp_humidity.split(',')
    print(f"Temperature: {temp}, Humidity: {humidity}")
    
    # Display the data on the LCD
    lcdDisplay.set(f"Temp: {temp} C   Hum: {humidity}%", 2)

client = mqtt.Client()
client.on_message = on_message

client.connect(SERVER, 1883, 60)
client.subscribe(TOPIC)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_start()

# Keep the script running
while True:
    time.sleep(1)