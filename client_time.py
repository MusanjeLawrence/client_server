import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set the port for the server to listen on
port = 9999

# connect to the server
clientsocket.connect((host, port))

# receive the current time from the server
current_time = clientsocket.recv(1024).decode('ascii')

print("The current time is %s" % current_time)

# close the client connection
clientsocket.close()
