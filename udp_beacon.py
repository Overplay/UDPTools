#!/usr/bin/env python
# usage: python udp_beacon.py [interval]

import socket
import sys, time
import microjson

PORT = 9091

def loadSettings():
    with open('config.json') as config_file:
        content = config_file.read()
        config = microjson.from_json(content)
        msg_data = {}
        msg_data['name'] = config['name']
        msg_data['location'] = config['location']
        return microjson.to_json(msg_data)

if (len(sys.argv) > 1):
    interval = int(sys.argv[1])
else:
    interval = 5

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('', 0))

print 'Message: ' + loadSettings()
print 'Interval:', interval

while 1:
    s.sendto(loadSettings(), ("<broadcast>", PORT))
    time.sleep(interval)
