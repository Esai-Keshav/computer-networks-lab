import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("", 6602))

a = input("ARP or RARP > ")

if a == "ARP":
    addr = input("enter ip =")
else:
    addr = input("enter mac = ")

s.send(addr.encode())

mac = s.recv(1024)

mac = mac.decode("utf-8")

if a == "ARP":
    print(f"MAC={mac} for IP => {addr}")
else:
    print(f"IP{mac} MAC = {addr}")
