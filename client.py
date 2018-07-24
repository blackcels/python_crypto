#!/usr/bin/python

import socket


class Client:
    def __init__(self, port, host):
        self.port = port
        self.host = host
        sock = socket.socket()
        #host = socket.gethostname()
        sock.connect((host, port))
        print ('Connected to', host)

        while True:
            message = input("Enter something for the server: ").encode()
            sock.send(message)
            # Halts
            print ('[Waiting for response...]')
            print (sock.recv(1024))
            