#!/usr/bin/env python
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.bind(("0.0.0.0", 8000))
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
clientSocket.listen(5)

(incomingSocket, address) = clientSocket.accept()
print "we got a connection from %s!" % (str(address))

googleSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
googleSocket.connect(("www.google.com", 80))

while True:
    # This half of the loop forwards from
    # client to google
    part = incomingSocket.recv(1024)
    if (len(part) > 0):
        print " > " + part
        googleSocket.sendall(part)
    else: # part will be "" when the connection is done
        exit(0)

    # This half of the loop forwards from
    # google to the client
    part = googleSocket.recv(1024)
    if (len(part) > 0):
        print " < " + part
        incomingSocket.sendall(part)
    else: # part will be "" when the connection is done
        exit(0)
