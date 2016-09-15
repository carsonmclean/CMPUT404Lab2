#!/usr/bin/env python
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("www.google.com", 80))

clientSocket.sendall("GET / HTTP/1.0\r\n\r\n")

while True:
    part = clientSocket.recv(1024)
    if (len(part) > 0):
        print part
