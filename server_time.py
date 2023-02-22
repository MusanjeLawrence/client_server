import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set the port for the server to listen on
port = 9999

# bind the socket to a public host, and a well-known port
serversocket.bind((host, port))

# set the server to listen for incoming connections
serversocket.listen(1)

while True:
    # establish a connection with a client
    clientsocket, address = serversocket.accept()

    print("Connection from: %s" % str(address))

    # get the current time as a string
    current_time = time.ctime(time.time()) + "\r\n"

    # send the current time to the client
    clientsocket.send(current_time.encode('ascii'))

    # close the client connection
    clientsocket.close()
