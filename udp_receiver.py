import socket
import sys

PORT = 9090 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', PORT))
 
while 1:
    data, addr = s.recvfrom(1024)
     
    if not data: 
        break
     
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
