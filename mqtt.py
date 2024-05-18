import time
import stomp


from rich import print

conn = None

class MQTT:
	conn = None
	def start_server():
		class MyListener(stomp.ConnectionListener):
		    def on_error(self, headers, message):
		        print('Received an error "%s"' % message)

		    def on_message(self, headers, message):
		        print('Received a message "%s"' % message)

		# Define your ActiveMQ connection parameters
		broker_url = 'tcp://localhost:1883'
		topic_name = '/topic/test'

		# Create a connection to ActiveMQ
		MQTT.conn = stomp.Connection([(broker_url)])

		# Set up a listener (optional)
		MQTT.conn.set_listener('', MyListener())

		# Connect to the broker
		MQTT.conn.connect(username='admin', password='admin')
		# Subscribe to a topic
		MQTT.conn.subscribe(destination=topic_name, id=1, ack='auto')
		# Wait for a while to receive messages (optional)
		
	def stop_server():
		time.sleep(2)
		# Disconnect from the broker
		MQTT.conn.disconnect()