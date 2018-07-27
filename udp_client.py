import socket
import sys

def parse_data(data):
	return data.split(',')

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.4.1', 8888)
message = 'start'

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    while True:
        data, server = sock.recvfrom(4096)
        print >>sys.stderr, 'received "%s"' % data
        print parse_data(data)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
