# mainframe
Mainframe configurations and server setup protocols.



## Server List

1. MQTT : Apache ActiveMQTT server for receiving and storing data.
2. NTP : Datetime synchronisation server.
3. DHCP: IP address allocation server.



## Scripts List

1. `main.py` : Starts all the servers in a specific sequence.
2. `mainframe monitor.py`: Keeps everything alive.
3. `install.py` : Installs all the binaries and python libraries that are required.
4.  ` mqtt.py` : MQTT library code.
5. `ntp.py`: NTP server code.
6. `dhcp.py`: DHCP server code.





## Testing

1. To test MQTT, we use HiveMQTT: 
	+ Server names: /scopes/m1, /scopes/m2, etc
	+ 
