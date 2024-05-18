from rich import print


from mqtt import MQTT


def run(action, *args, **kwargs):
	print(f"Running: {action}")
	action(*args, **kwargs)



## Run mqtt
run(MQTT.start_server)