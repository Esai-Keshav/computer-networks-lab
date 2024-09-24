import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # Port number

    # create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"UDP Server listening on {host}:{port}")

    while True:
        # receive data from client (1024 bytes buffer)
        data, address = server_socket.recvfrom(1024)
        data = data.decode()

        if not data:
            # if no data is received, break
            break

        print(f"Received from {address}: {data}")

        # Respond to the client
        data = input(" -> ")
        server_socket.sendto(data.encode(), address)


if __name__ == "__main__":
    server_program()
