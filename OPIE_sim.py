#!/usr/bin/env python
# usage: python OPIE_sim.py [number of OPIEs] [broadcast interval]

import socket
import sys, time
import microjson

PORT = 9091

def loadSettings(i):
    with open('config.json') as config_file:
        content = config_file.read()
        config = microjson.from_json(content)
        msg_data = {}
        msg_data['name'] = config['name'] + str(i)
        msg_data['location'] = config['location'] + str(i)
        msg_data['mac'] = str(i)+':'+str(i)
        return microjson.to_json(msg_data)

def main():
    if (len(sys.argv) > 1):
        numOPIEs = int(sys.argv[1])
    else:
        numOPIEs = 5

    if (len(sys.argv) > 2):
        interval = int(sys.argv[2])
    else:
        interval = 5

    sockets = []
    for i in range(numOPIEs):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind(('', 0))
        sockets.append(s)

        print 'Message: ' + loadSettings(i)
        print 'Interval:', interval

    counter = 0
    while 1:
        for (i, s) in enumerate(sockets):
            if counter in range(2,7) and i == 2:
                pass
            else:
                s.sendto(loadSettings(i), ("<broadcast>", PORT))
        time.sleep(interval)
        counter += 1

if __name__ == "__main__":
    main()
