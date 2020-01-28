import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',9000))
msg,addr = server.recvfrom(1024)
print(msg.decode())
server.sendto('udp server'.encode(),addr)
server.close()