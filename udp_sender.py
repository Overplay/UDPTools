
# usage: python udp_sender.py [interval]

import socket
import sys, time
import json

PORT = 8888

with open('config.json') as config_file:
	config = json.load(config_file)
	msg_data = {}
	msg_data['name'] = config['name']
	msg_data['location'] = config['location']
	msg = json.dumps(msg_data)

if (len(sys.argv) > 1):
	interval = int(sys.argv[1])
else:
	interval = 5

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('', 0))

print 'Message: ' + msg
print 'Interval:', interval
 
while 1:
    s.sendto(msg, ("<broadcast>", PORT))
    time.sleep(interval)