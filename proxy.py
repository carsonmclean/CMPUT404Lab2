#!/usr/bin/env python
import socket
import os

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.bind(("0.0.0.0", 8000))
clientSocket.listen(5)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
    (incomingSocket, address) = clientSocket.accept()
    print "we got a connection from %s!" % (str(address))

    pid = os.fork()
    if (pid == 0): # we must be the child (clone) process, so we will handle proxying for this client


        googleSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        googleSocket.connect(("www.google.ca", 80))

        incomingSocket.setblocking(0)
        googleSocket.setblocking(0)

        while True:
            # This half of the loop forwards from
            # client to google
            skip = False
            try:
                part = incomingSocket.recv(1024)
            except socket.error, exception:
                if exception.errno == 35:
                    skip = True
                else:
                    raise
            if not skip:
                if (len(part) > 0):
                    print " > " + part
                    googleSocket.sendall(part)
                else: # part will be "" when the connection is done
                    exit(0)

            # This half of the loop forwards from
            # google to the client
            skip = False
            try:
                part = googleSocket.recv(1024)
            except socket.error, exception:
                if exception.errno == 35:
                    skip = True
                else:
                    raise
            if not skip:
                if (len(part) > 0):
                    print " < " + part
                    incomingSocket.sendall(part)
                else: # part will be "" when the connection is done
                    exit(0)
