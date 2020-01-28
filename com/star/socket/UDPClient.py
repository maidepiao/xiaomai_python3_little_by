import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto('udp client'.encode(),('127.0.0.1',9000))
print(client.recv(1024).decode())
client.close()