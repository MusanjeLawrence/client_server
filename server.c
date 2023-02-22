#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <time.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <port>\n", argv[0]);
        exit(1);
    }

    // Create a socket
    int server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Error creating socket");
        exit(1);
    }

    // Specify the server address and port
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = htonl(INADDR_ANY);
    server_address.sin_port = htons(atoi(argv[1]));

    // Bind the socket to the server address and port
    if (bind(server_socket, (struct sockaddr *)&server_address, sizeof(server_address)) == -1) {
        perror("Error binding socket");
        exit(1);
    }

    // Listen for incoming connections
    if (listen(server_socket, 5) == -1) {
        perror("Error listening for incoming connections");
        exit(1);
    }

    while (1) {
        // Accept a client connection
        int client_socket = accept(server_socket, NULL, NULL);
        if (client_socket == -1) {
            perror("Error accepting client connection");
            exit(1);
        }

        // Get the current time
        time_t timestamp = time(NULL);

        // Send the timestamp to the client
        if (send(client_socket, &timestamp, sizeof(timestamp), 0) == -1) {
            perror("Error sending timestamp to client");
            exit(1);
        }

        // Close the client socket
        close(client_socket);
    }

    // Close the server socket
    close(server_socket);

    return 0;
}
