import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 4444))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print("Connected by", address)
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print("Message from client:", data)
    if data == "Bye.":
        break

client_socket.close()
server_socket.close()
