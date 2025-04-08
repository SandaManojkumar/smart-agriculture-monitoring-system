import time
import random
import json
import paho.mqtt.client as mqtt

broker = "aj4opo762y2c4-ats.iot.ap-south-1.amazonaws.com"
port = 8883
topic = "agriculture/sensors"
client_id = "AgriSimDevice"

ca = "AmazonRootCA1.pem"
cert = "certificate.pem.crt"
key = "private.pem.key"

client = mqtt.Client(client_id=client_id)
client.tls_set(ca, certfile=cert, keyfile=key)
client.connect(broker, port)
client.loop_start()

while True:
    data = {
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "soil_moisture": round(random.uniform(20, 60), 2),
        "timestamp": int(time.time())
    }
    client.publish(topic, json.dumps(data), qos=1)
    print("Published:", data)
    time.sleep(5)
