import paho.mqtt.client as mqtt

# Callback when connected to MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker with code: " + str(rc))
        # Subscribe to the topic
        client.subscribe("/laurent/light_control")
    else:
        print("Connection failed with code: " + str(rc))

# Callback when message is received
def on_message(client, userdata, msg):
    state = msg.payload.decode()
    if state == "ON":
        print("💡 Light is TURNED ON")
    elif state == "OFF":
        print("💡 Light is TURNED OFF")
    else:
        print(f"Received unknown command: {state}")

# Set up MQTT client
client = mqtt.Client()

# Use MQTT over TCP instead of WebSocket for Python client
client.on_connect = on_connect
client.on_message = on_message

# Connect to specified MQTT broker (using TCP port 1883)
broker_address = "157.173.101.159"
client.connect(broker_address, 1883, 60)

# Start the loop
print("Starting IoT Light Simulation...")
try:
    client.loop_forever()
except Exception as e:
    print(f"Error: {e}")