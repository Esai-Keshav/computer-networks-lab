import socket


def client_program():
    print('Type "bye" to terminate.')
    host = socket.gethostname()  # Server's hostname or IP
    port = 5000  # Port number

    # create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input(" -> ")  # Input message to send

    while message.lower().strip() != "bye":
        # send message to the server
        client_socket.sendto(message.encode(), (host, port))

        # receive server's response
        data, _ = client_socket.recvfrom(1024)
        print("Received from server: " + data.decode())

        message = input(" -> ")  # Input next message

    client_socket.close()  # Close the connection


if __name__ == "__main__":
    client_program()
