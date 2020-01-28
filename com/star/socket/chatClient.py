import socket
import pickle
from star.socket.msg import ChatMsg,BindMsg
from threading import Thread

class ChatClient:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.user_id = None
    def read(self,socket_):
        while True:
            recv_msg = pickle.loads(socket_.recv(1024))
            print('用户:{:s},发来消息:{:s}'.format(recv_msg.from_user_id,recv_msg.content))
            if recv_msg.content == 'quit':
                break
    def write(self,socket_):
        while True:
            to_user_id = input('请输入对方聊天账号:\r\n')
            content = input('请输入发送内容:\r\n')
            if content == 'quit':
                break
            chat_ = ChatMsg(self.user_id, to_user_id, content)
            socket_.send(pickle.dumps(chat_))
    def connect(self):
        self.user_id = input('请输入您的账号:\r\n')
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        bind_ = BindMsg(self.user_id)
        client.send(pickle.dumps(bind_))
        r = Thread(target=self.read,args=(client,))
        r.start()
        w = Thread(target=self.write,args=(client,))
        w.start()

if __name__ == '__main__':
    ChatClient('127.0.0.1',9000).connect()