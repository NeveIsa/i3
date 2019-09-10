import paho.mqtt.client as mqtt
import subprocess
import datetime
import time



broker="18.219.4.146"
broker_port=1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribed = on_subscribed
client.on_log = on_log

client.username_pw_set("sampad_buyer", "ywqk7po0zk9q")
client.connect(broker, broker_port, timeout_reconnect)
