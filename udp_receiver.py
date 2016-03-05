import socket
import sys

UDP_HOST = '127.0.0.1'
UDP_PORT = 8888

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error, msg:
	print 'Failed to create socket. Error Code: ' + str(msg[0]) + ' Message: ' + msg[1]
	sys.exit()

try:
    sock.bind((UDP_HOST, UDP_PORT))
    print 'Socket bind complete'
except socket.error, msg:
    print 'Bind failed. Error Code: ' + str(msg[0]) + ' Message: ' + msg[1]
    sys.exit()
 
while 1:
    data, addr = sock.recvfrom(1024)
     
    if not data: 
        break
     
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()