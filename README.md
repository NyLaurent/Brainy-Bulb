# MQTT Light Control Simulation

This project implements a simple IoT light control system using MQTT protocol with a specific broker.

## Components
1. `index.html`: Web interface with ON/OFF buttons and status display
2. `light_simulation.py`: Python script simulating an ESP8266 IoT device

## Setup Instructions
1. Prerequisites:
   - Python 3.x
   - paho-mqtt library (`pip install paho-mqtt`)
   - A modern web browser
   - Access to MQTT broker at 157.173.101.159

2. Running the simulation:
   - Start the Python script: `python light_simulation.py`
   - Open `index.html` in a web browser
   - Click the buttons to control the simulated light

## How It Works
- Web interface connects via WebSocket (ws://157.173.101.159:9001)
- Python client connects via TCP (157.173.101.159:1883)
- Buttons publish "ON" or "OFF" to `/student_group/light_control`
- Python script subscribes and prints light status

## Testing
- Requires connection to the specified MQTT broker
- Web client uses port 9001 (WebSocket)
- Python client uses port 1883 (TCP)
- Ensure firewall allows connections to these ports

## Notes
- Assumes MQTT broker is running at 157.173.101.159
- Web client uses WebSocket protocol (port 9001)
- Python client uses standard MQTT over TCP (port 1883)
- No authentication implemented in this example# Brainy-Bulb
