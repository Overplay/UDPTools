#!/usr/bin/env python
# usage: python mac_sim.py [number of OPIEs] [broadcast interval]

import socket
import sys, time
import microjson

MCAST_GROUP = '224.1.1.1'
MCAST_PORT = 5007
LOCS = ["Over Bar", "Darts", "Pool Table", "Back Room", "Patio", "Deck"]
MACS = ["01-23-45-67-89-ab", '23-53-c3-g4-34-55', '11-22-33-44-55-66', 
        'a4-5g-ff-33-5f-63', '23-54-g5-e3-66-3f', '00-44-77-42-22-65']

def loadSettings(i):
    with open('config.json') as config_file:
        content = config_file.read()
        config = microjson.from_json(content)
        msg_data = {}
        msg_data['name'] = config['name'] + str(i)
        msg_data['location'] = LOCS[i % len(LOCS)]
        msg_data['mac'] = MACS[i % len(MACS)]
        return microjson.to_json(msg_data)

def main():
    if (len(sys.argv) > 1):
        numOPIEs = int(sys.argv[1])
    else:
        numOPIEs = len(LOCS)

    if (len(sys.argv) > 2):
        interval = int(sys.argv[2])
    else:
        interval = 5

    # addrinfo = socket.getaddrinfo(MCAST_GROUP, None)[0]
    # s = socket.socket(addrinfo[0], socket.SOCK_DGRAM)

    sockets = []

    for i in range(numOPIEs):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        sockets.append(s)

        print 'Message: ' + loadSettings(i)
        print 'Interval:', interval

    counter = 0
    while 1:
        for (i, s) in enumerate(sockets):
            if counter in range(2,7) and i == 2:
                pass
            else:
               s.sendto(loadSettings(i), (MCAST_GROUP, MCAST_PORT))
        time.sleep(interval)
        counter += 1

if __name__ == "__main__":
    main()
