import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8888))
msg='我是小麦'
client.send(msg.encode(encoding='utf-8'))
recv = client.recv(1024).decode(encoding='utf-8')
print(recv)
client.close()

