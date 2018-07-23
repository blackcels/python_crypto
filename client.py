#!/usr/bin/python

import socket

sock = socket.socket()
host = socket.gethostname()
port = 12220

sock.connect((host, port))
print ('Connected to', host)

while True:
    message = input("Enter something for the server: ").encode()
    sock.send(message)
    # Halts
    print ('[Waiting for response...]')
    print (sock.recv(1024))