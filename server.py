import socket

sock = socket.socket()
host = socket.gethostname()
port = 12220
sock.bind((host, port))

sock.listen(5)
connector = None

while True:
   if connector is None:
       # Halt
       print ('[Waiting for connection...]')
       connector, addr = sock.accept()
       print ('Got connection from', addr)
   else:
       # Halt
       print ('[Waiting for response...]')
       print (connector.recv(1024))
       message = input("Enter something to this client: ").encode()
       connector.send(message)