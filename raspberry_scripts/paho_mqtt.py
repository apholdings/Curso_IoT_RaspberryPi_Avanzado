import paho.mqtt.client as mqtt

# El callback para cuando el cliente recibe una respuesta CONNACK del servidor.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Suscribirse en on_connect() significa que si perdemos la conexión y
    # se vuelve a conectar se renuevan las suscripciones.
    client.subscribe("some/topic")

# El callback para cuando se recibe un mensaje PUBLISH del servidor.
def on_message(client, userdata, msg):
    # Hacer algo aqui si el mensaje es X o Y
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

# Llamada de bloqueo que procesa el trafico de red, despacha callbacks y
# maneja la reconexión.
# Hay otras funciones loop*() disponibles que ofrecen una interfaz de hilos y una
# interfaz manual.
client.loop_forever()