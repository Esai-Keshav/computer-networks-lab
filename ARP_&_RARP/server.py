import socket

table = {"ip 1": "mac 1", "ip 2": "mac 2"}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", 6602))
s.listen()

conn, addr = s.accept()

ip = conn.recv(1024)

ip = ip.decode("utf-8")

mac = table.get(ip, "No entry")

conn.send(mac.encode())
