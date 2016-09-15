#!/usr/bin/env python
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.bind(("0.0.0.0", 8000))
clientSocket.listen(5)

(socket, address) = clientSocket.accept()
print "we got a connection from %s!" % (str(address))
