import socket,pickle,json
import threading
from star.socket.msg import ChatMsg,BindMsg

class ChatServer:
    addr_dict = {}
    conn_dict = {}
    def __init__(self,host,port):
        self.host = host
        self.port = port
    def open(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen()
        while True:
            client_socket,client_addr = server.accept()
            client_addr_str = '[%s:%d]'%client_addr
            print('客户端%s已连接'%client_addr_str)
            t = threading.Thread(target=self.__run,args=(client_socket,client_addr))
            t.start()
    def __run(self,*args):
        socket_,addr_ = args
        recv_msg = pickle.loads(socket_.recv(1024))
        while recv_msg:
            if isinstance(recv_msg,BindMsg):
                ChatServer.addr_dict[recv_msg.user_id] = addr_
                ChatServer.conn_dict[recv_msg.user_id] = socket_
                user_ids_ = ''
                for user_id_ in ChatServer.conn_dict.keys():
                    user_ids_ += (user_id_+',')
                notify_msg = ChatMsg('server','client','当前在线用户[%s]'%user_ids_[:-1])
                for conn in ChatServer.conn_dict.values():
                    conn.send(pickle.dumps(notify_msg))
            elif isinstance(recv_msg,ChatMsg):
                to_ = recv_msg.to_user_id
                ChatServer.conn_dict[to_].send(pickle.dumps(recv_msg))
            print(json.dumps(recv_msg, default=lambda obj: obj.__dict__))
            recv_msg = pickle.loads(socket_.recv(1024))

if __name__ == '__main__':
    ChatServer('127.0.0.1',9000).open()
