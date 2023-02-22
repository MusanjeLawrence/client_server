import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 4444))

while True:
    message = input("Enter a message to send to the server (type 'Bye.' to exit):")
    client_socket.sendall(message.encode())
    if message == "Bye.":
        break

client_socket.close()
