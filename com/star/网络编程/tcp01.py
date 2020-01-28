#coding:utf-8
import socket

sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sc.bind(('127.0.0.1',8888))
sc.listen(5)
while True:
    conn,addr = sc.accept()
    data = conn.recv(1024)
    print(addr,data.decode(encoding='utf-8'))
    conn.sendall(b'HTTP/1.1 200 OK \r\n\r\n'+'你好，小麦'.encode(encoding='utf-8'))
    conn.close()