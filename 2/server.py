import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port number above 1024

    # create socket instance
    server_socket = socket.socket()

    # bind host address and port together
    server_socket.bind((host, port))

    # configure how many clients the server can listen to simultaneously
    server_socket.listen(2)

    # accept new connection
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        # receive data stream. It won't accept data packets greater than 1024 bytes
        data = conn.recv(1024).decode()

        if not data:
            # if no data is received, break
            break

        print("from connected user: " + str(data))

        # get input from server side to send to client
        data = input(" -> ")

        # send data to the client
        conn.send(data.encode())

    # close the connection
    conn.close()


if __name__ == "__main__":
    server_program()
