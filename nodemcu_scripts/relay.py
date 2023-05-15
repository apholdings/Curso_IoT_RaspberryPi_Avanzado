"""
Este script se conecta al broker MQTT, se suscribe al tema 'relay', y entra en un bucle 
que comprueba si hay nuevos mensajes cada segundo. Cuando se recibe un mensaje, se llama a la función de devolución de llamada 
sub_cb() con el tema y el mensaje como argumentos. Si el mensaje es 'on', el relé se enciende. 
el relé, y si es 'off', lo apaga.

Recuerda sustituir 'mqtt_broker_ip' por la dirección IP de tu broker MQTT. También tenga en cuenta que 
la función machine.rng() utilizada para generar un ID de cliente aleatorio puede no estar disponible en todas las plataformas MicroPython. 
plataformas MicroPython.

"""

import machine
import time
from umqtt.simple import MQTTClient

# create a random MQTT clientID
random_num = machine.rng() & 0xff
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')

# Connect to the relay
relay = machine.Pin(16, machine.Pin.OUT)

# Connect to the MQTT broker
client = MQTTClient(mqtt_client_id, 'mqtt_broker_ip')  # replace 'mqtt_broker_ip' with the IP of your MQTT broker

# Define a callback function to handle received messages
def sub_cb(topic, msg):
    print((topic, msg))
    if msg == b'on':
        relay.off()
    elif msg == b'off':
        relay.on()

client.set_callback(sub_cb)

# Connect to the broker and subscribe to the topic
client.connect()
client.subscribe(b'relay')

# Main loop to check for new messages
while True:
    client.check_msg()
    time.sleep(1)


