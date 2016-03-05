
# usage: python udp_sender.py [interval]

import socket
import sys, time
import json

with open('config.json') as config_file:
	config = json.load(config_file)

	udp_host = config['udp_host']
	udp_port = config['udp_port']

	msg_data = {}
	msg_data['name'] = config['name']
	msg_data['location'] = config['location']
	msg = json.dumps(msg_data)

if (len(sys.argv) > 1):
	interval = int(sys.argv[1])
else:
	interval = 5

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created.'
except socket.error, msg:
	print 'Failed to create socket. Error Code: ' + str(msg[0]) + ' Message: ' + msg[1]
	sys.exit()

print 'Message: ' + msg
print 'Sending message to {}:{} every {} sec.'.format(udp_host, udp_port, interval)
 
while 1:
    sock.sendto(msg, (udp_host, udp_port))
    time.sleep(interval)