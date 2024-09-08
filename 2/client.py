import socket


def client_program():
    print('Type "bye" to terminate')

    host = socket.gethostname()  # as both server and client are running on the same PC
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate socket
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take initial input

    while message.lower().strip() != "bye":
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print("Received from server: " + data)  # display server response

        message = input(" -> ")  # take next input

    # close the connection
    client_socket.close()


if __name__ == "__main__":
    client_program()
