import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish("some/topic", "Hello world!")

def on_publish(client, userdata, mid):
    print("Message ID: "+str(mid))

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Si nosotros somos el broker enviando el mensaje al componente entonces se pone localhost, 
# si no, debes poner el IP del broker
client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_start()